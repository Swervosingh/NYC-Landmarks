import React from 'react';
import { BrowserRouter as Router, Route, Switch, Link } from 'react-router-dom';
import Navbar from './Navbar';
import Home from './Home';
import Locations from './Locations';
import Pictures from './Pictures';
import MapPage from './MapPage'; // Import the MapPage component

function App() {
  return (
    <Router>
      <div className="App">
        <Navbar />
        <Switch>
          <Route exact path="/" component={Home} />
          <Route path="/locations" component={Locations} />
          <Route path="/pictures" component={Pictures} />
          <Route path="/map" component={MapPage} /> 
        </Switch>
      </div>
    </Router>
  );
}

export default App;

