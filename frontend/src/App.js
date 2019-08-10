import React from 'react';
import logo from './logo.svg';
import './css/App.css';
import './css/Map.css';

import WebMap from './Map'

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <p>
          Livability
        </p>
      </header>
      <div className="ui container"> 
        <div className="ui grid">
          <div className="row">
            <div className="column smallmap">
              <WebMap />
            </div>
            <div className="column">
              Details
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}


export default App;
