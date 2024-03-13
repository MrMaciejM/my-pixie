import {Pool} from "pg";

// db name = pixie-db

// environment variables for passwords 
// i.e. exporting env variables 

// Database connection configuration
const db = new Pool({
  user: 'postgres',
  host: 'localhost',
  database: 'pixie-db',
  password: 'admin', // DON'T DO THIS - TESTING ONLY
  port: 5432, // Default PostgreSQL port
});

// test db connection 
(async () => {
  try {
    // Attempt to connect to the database
    const client = await db.connect();
    console.log('Connected to the database\n');

    // Release the client back to the pool
    client.release();
  } catch (error) {
    console.error('Error connecting to the database');
  } finally {
    // Close the pool to close all connections
    db.end();
  }
})();
// (); invokes immediately async function 

// Todo: 
// Write test / insert data 
const myID = 1
try {
    const client = await db.connect()
    const myQuery = await client.query('SELECT username FROM users')
    const users = myQuery
    client.release()
    console.log("RESULT: ");
} catch (error) {
    console.log(error);
}






