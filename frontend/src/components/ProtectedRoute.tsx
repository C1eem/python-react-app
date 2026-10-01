import React, { useEffect, useState } from "react";
import { Navigate } from "react-router-dom";

type Props =    {
    children: React.ReactNode
}


export function ProtectedRoute({children}: Props) {
    const [user, setUser] = useState<unknown>(null)
    const [loading, setLoading] = useState(true)

    useEffect(() => {
        fetch("http://localhost:8000/users/me", {
            credentials: "include",
        })
        .then((res) => (res.ok? res.json() : null))
        .then((data) => setUser(data))
        .finally(() => setLoading(false))
    }, [])

    if (loading) return <p>Загрузка</p>
    if (!user) return <Navigate to="/login" replace />
    
    return <>{children}</>
}