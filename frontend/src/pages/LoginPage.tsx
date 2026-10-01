import { useState } from "react"
import { useNavigate } from "react-router-dom"


export function LoginPage() {
    const navigate = useNavigate()
    const [email, setEmail] = useState("")
    const [password, setPassword] = useState("")
    const [loading, setLoading] = useState(false)
    const [error, setError] = useState<string | null>(null)

    async function handleSubmit(e: React.FormEvent<HTMLFormElement>) {
        e.preventDefault()
        setLoading(true)
        setError(null)

        try {
            const res = await fetch("http://localhost:8000/auth/login", {
                method: "POST",
                credentials: "include",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({email, password}),
            })

            if (!res.ok) {
                throw new Error(res.status === 401 ? "Неверный логин или пароль" : `Ошибка ${res.status}`)
            }

            navigate("/")
        } catch (e) {
            setError(e instanceof Error ? e.message : "Неизвестная ошибка")
        } finally {
            setLoading(false)
        }
    }
    
    return (
        <form onSubmit={handleSubmit}>
            <h1>Вход</h1>

            <input
                placeholder="Email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
            />
            <input
                type="password"
                placeholder="Пароль"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
            />

            <button type="submit" disabled={loading}>
                {loading ? "Вход..." : "Войти"}
            </button>

            {error && <p style={{color: "red"}}>{error}</p>}
            
        </form>
    )
}