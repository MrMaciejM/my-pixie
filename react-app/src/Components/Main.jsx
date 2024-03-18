import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import "../App.css"
import "./Main.css"

function Main() {

    return (
        <Container className=" mainContainer aaa">
            <Row>
                <Col></Col>
                 <h3>Some Long Random Title</h3>
                 <h5>username username</h5>
                <p className='text-left'>Post text content MAIN. Lorem ipsum dolor sit amet consectetur adipisicing elit. Velit accusantium nam, enim numquam esse earum, et nostrum adipisci iste cum dignissimos veniam iure id sed sunt natus possimus ea! Dolor!</p>                    
            </Row>
    </Container>
    )
}

export default Main