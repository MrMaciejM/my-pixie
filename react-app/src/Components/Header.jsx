import Container from "react-bootstrap/Container";
import Nav from "react-bootstrap/Nav";
import Navbar from "react-bootstrap/Navbar";

function Header() {

    return (
        <>
      <Navbar fixed="top" bg="primary" data-bs-theme="dark" >
        <Container className="justify-content-end">
          <Nav className="">
            <Nav.Link href="#home">Posts</Nav.Link>
            <Nav.Link href="#features">News</Nav.Link>
            <Nav.Link href="#pricing">Sign In</Nav.Link>
          </Nav>
        </Container>
      </Navbar>      
    </>
    );
        
    
}

export default Header