import { useEffect, useState } from 'react'
// import logo from './logo.svg';
import axios from 'axios'
import './App.css';

function App() {
  const [resData, setResData] = useState(null)
  useEffect(() => {
    axios.get('http://localhost:8000/api/reporting/order-dev/')
    .then(res => {
      console.log(res)
    })
    .catch(err => {
      console.error(err)
    })
  }, [])
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Order Report
        </p>
      </header>
    </div>
  );
}

export default App;
