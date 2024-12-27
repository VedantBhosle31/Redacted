import { useState } from 'react'
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'
import './App.css'
import Home from './pages/Home'
import Nav from './components/Nav'
import Validate from './pages/Validate'

function App() {
  const [count, setCount] = useState(0)

  return (
    <Router>
      <Nav />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/validate" element={<Validate />} />
      </Routes>
    </Router>
  )
}

export default App
