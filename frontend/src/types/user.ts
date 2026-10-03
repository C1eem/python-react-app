export type UserRole = "parent" | "student" | "teacher" | "admin"

export type UserFormValues = {
    email: string
    password: string
    first_name: string
    last_name: string
    middle_name: string | null
}

export type User = {
    id: number
    email: string
    firstName: string
    lastName: string
    middleName: string | null
    role: UserRole
}