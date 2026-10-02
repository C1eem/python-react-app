import { useNavigate } from "react-router-dom"

export function DashboardPage() {
    const navigate = useNavigate()

    async function handleLogout() {
        await fetch("http://localhost:8000/auth/logout", {
        method: "POST",
        credentials: "include",
        })
        navigate("/login")
    }

    return (
        <div>
        <h1>Дашборд</h1>
        <button onClick={handleLogout}>Выйти</button>
        </div>
    )
}