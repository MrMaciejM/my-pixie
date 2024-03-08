import {Pool} from "pg";

// configure PostgreSQL connection 
const pool = new Pool({
    user: "postgres",
    host: "localhost",
    database: "postgres",
    port: "5432"
})