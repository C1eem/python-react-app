import { useState } from "react"
import type { UserFormValues, User } from "../types/user"

export function UserForm() {
    const [form, setForm] = useState<UserFormValues>({
        email: "",
        password: "",
        firstName: "",
        lastName: "",
        middleName: null,
    })

    function handleChange(e: React.ChangeEvent<HTMLInputElement>) {
        setForm((prev) => ({ ...prev, email: e.target.value }))
        
    }

    async function handleSubmit(e: React.FormEvent<HTMLFormElement>) {
        e.preventDefault()
        const payload = {
            email: form.email,
            password: form.password,
            first_name: form.firstName,
            last_name: form.lastName,
            middle_name: form.middleName,
            }
        const res = await fetch("http://localhost:8000/users/", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload),   // ← form уже заполнен через onChange
        })
        
        if (res.ok){
            const created = await res.json()
            console.log("создан", created)
        } else {
            console.log("ошибка", res.status)
        }

    }

    return (
        <form onSubmit={handleSubmit}>
            <input value={form.email} onChange={handleChange} />
            <button type="submit">Создать</button>
        </form>
    )
}

