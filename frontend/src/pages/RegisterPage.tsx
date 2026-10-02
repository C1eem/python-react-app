import { useState } from "react"
import type { UserFormValues } from "../types/user"
import { useNavigate } from "react-router-dom"

export function RegisterPage() {

    const navigate = useNavigate()

    const [form, setForm] = useState<UserFormValues>({
        email: "",
        password: "",
        first_name: "",
        last_name: "",
        middle_name: null,
    })
    const [loading, setLoading] = useState(false)
    const [error, setError] = useState<string | null>(null)

    function handleChange(
        e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>
    ) {
        const { name, value } = e.target
        setForm((prev) => ({
            ...prev,
            [name]: value === "" && name === "middle_name" ? null : value,
        }))
    }

    async function handleSubmit(e: React.FormEvent<HTMLFormElement>) {
        e.preventDefault()
        setLoading(true)
        setError(null)

        try {
            const res = await fetch("http://localhost:8000/users/", {
                method: "POST",
                credentials: "include",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(form),
            })

            if (!res.ok) {
                throw new Error(`Ошибка регистрации: ${res.status}`)
            }

            navigate("/login")
        } catch (e) {
            setError(e instanceof Error ? e.message : "Неизвестная ошибка")
        } finally {
            setLoading(false)
        }
    }

    return (
    <form onSubmit={handleSubmit}>
    <h1>Регистрация</h1>

    <input
        name="email"
        type="email"
        placeholder="Email"
        value={form.email}
        onChange={handleChange}
    />

    <input
        name="password"
        type="password"
        placeholder="Пароль"
        value={form.password}
        onChange={handleChange}
    />

    <input
        name="first_name"
        placeholder="Имя"
        value={form.first_name}
        onChange={handleChange}
    />

    <input
        name="last_name"
        placeholder="Фамилия"
        value={form.last_name}
        onChange={handleChange}
    />

    <input
        name="middle_name"
        placeholder="Отчество (необязательно)"
        value={form.middle_name ?? ""}
        onChange={handleChange}
    />

    <button type="submit" disabled={loading}>
        {loading ? "Регистрация…" : "Зарегистрироваться"}
    </button>

    {error && <p style={{ color: "red" }}>{error}</p>}
    </form>
)
}