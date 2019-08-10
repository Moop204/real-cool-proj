import React from 'react';
import logo from './logo.svg';
import './css/App.css';

import Map from './Map'

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <p>
          Livability
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
      <div class="ui container"> 
        <div class="ui grid">
          <div class="row">
            <div class="column">
              <Map />
            </div>
            <div class="column">
              KEY FEATURES
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}


export default App;
