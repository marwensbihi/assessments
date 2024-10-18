import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './components/home'
import SearchResults from './components/SearchResults';
import NearbyAirports from './components/NearbyAirports';

function App() {
  return (
    <Router>
      <div className="App">
        <Routes>
          <Route path="/" element={<Home/>} />
          <Route path="/search" element={<SearchResults />} />
          <Route path="/nearby-airports" element={<NearbyAirports />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
