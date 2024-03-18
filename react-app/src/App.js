import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Header from "./Components/Header.jsx"
import Main from "./Components/Main.jsx"
import Trending from "./Components/Trending.jsx"
import NewsWeather from "./Components/NewsWeather.jsx"


function App() {
  return (
    <div>    
      <Header />
      <Container >
        <Row>
          <Col>
            <Main  />           
          </Col>
        </Row>
      </Container>
    </div>
  );
}

export default App;
