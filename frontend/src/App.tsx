import { Routes, Route, Link } from "react-router-dom"
import { LoginPage } from "./pages/LoginPage"
import { RegisterPage } from "./pages/RegisterPage"
import { DashboardPage } from "./pages/DashboardPage"
import { ProtectedRoute } from "./components/ProtectedRoute"

function App() {
  return (
    <div>
      <nav>
        <Link to="/" >Дашборд</Link> |{" "}
        <Link to="/login" >Логин</Link> |{" "}
        <Link to="/register" >Регистрация</Link>
      </nav>

      <Routes>
        <Route path="/login" element={<LoginPage />} />
        <Route path="/register" element={<RegisterPage />} />
        <Route path="/" element={
            <ProtectedRoute>
              <DashboardPage />
            </ProtectedRoute>
        }/>
      </Routes>
    </div>
  )
}

export default App