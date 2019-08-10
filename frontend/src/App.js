import React from 'react';
import { Grid, Image } from 'semantic-ui-react'
import './css/App.css';
import './css/Map.css';

import AppGrid from './Grid'


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
          <AppGrid />
        </div>
      </div>
    </div>
  );
}


export default App;
