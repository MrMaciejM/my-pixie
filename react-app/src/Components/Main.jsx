import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import "../App.css"
import "./Main.css"
import React, { useEffect, useState } from 'react';

function Main() {

    // http://localhost:3000/

    // This will be populated with fetched data 
    const [data, setData] = useState({
        name: "",
        date: ""
    })

    // Fetch data from backend - TESTING PHASE ONLY FOR NOW
    useEffect(() => {
        fetch("/home").then((res) =>
            // convert to JSON format 
            res.json().then((data) => {
                console.log(data);
                // filter time data e.g. 18:30
                let filteredTime = data[0][1]["date_posted"].substr(0, 5)
                let filteredUsername = data[1]["username"]
                setData({
                    name: filteredUsername,
                    date: filteredTime
                })
        })).catch((error) => {
            console.error("Error fetching data:", error)
        })
    })

    return (
        <Container className=" mainContainer aaa">
            <Row>
                <Col></Col>
                 <p>Posted: {data.date}</p>
                 <p>User: {data.name}</p>
                 <h3>Some Long Random Title</h3>
                <p className='text-left'>Post text content MAIN. Lorem ipsum dolor sit amet consectetur adipisicing elit. Velit accusantium nam, enim numquam esse earum, et nostrum adipisci iste cum dignissimos veniam iure id sed sunt natus possimus ea! Dolor!</p>    
                <button>Edit</button>
                <div></div>               
                <button className='deleteBtn'>Delete</button>
            </Row>
            
    </Container>
    )
}

export default Main