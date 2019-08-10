
import React, { Component, createRef } from 'react'
import { Map, Marker, Popup, TileLayer } from 'react-leaflet'
import './css/Map.css';
import GoogleMap from 'google-map-react'


/*
type State = {
  lat: number,
  lng: number,
  zoom: number,
}
*/

/*
{
  lat: float
  lng: float
}
*/

export default class WebMap extends Component { 
  constructor(props) {
    super(props)

    //this.googleMapRef = createRef()
  }

  static defaultProps = {
    center:[59, 30],
    zoom: 9,

  }

  /*
  getChildren = () => {
    children = fetch('localhost:5000/main')
    .then(response => response.json())
    .then((jsonData) => {
      console.log(jsonData)
    })
    .catch((error) => {
      console.error(error)
    })
    this.markers = children
    // idk 
  }
  */

  createGoogleMap = () => {
    
    return (<GoogleMap 
      bootstrapURLKeys={{
        key: 'AIzaSyCpjzJHDP2EOQH6_AAFOT-xzcQ7y2hyrHI',
        language: 'en',
        region: 'au'
      }}
      //{this.markers.map(c => <Marker name={c.name} lat={c.lat} lng={c.lng}/> )}
    />)
    /*
    new window.google.maps.Map(this.googleMapRef.current, {
      zoom: 12,
      center: {
        lat: -33.82,
        lng: 151,
      },
      disableDefaultUI: true,
    })
    */   
  }

  render() {
    return (
      <div id="google-map" style={{ width:'1200px', height:'800px'}}>
        <GoogleMap 
        bootstrapURLKeys={{
          key: 'AIzaSyCpjzJHDP2EOQH6_AAFOT-xzcQ7y2hyrHI',
          language: 'en',
          region: 'au',
        }}
        center={[-33.82, 151.0]}
        zoom={9}
        />
      </div>
    )
  }
  
  // componentDidMount = () => {
  //   const googleScript = document.createElement('script')
  //   googleScript.src = `https://maps.googleapis.com/maps/api/js?key=AIzaSyCpjzJHDP2EOQH6_AAFOT-xzcQ7y2hyrHI&libraries=places`
  //   window.document.body.appendChild(googleScript)
  //   googleScript.addEventListener('load', () => {
  //     this.googleMap = this.createGoogleMap()
  //   })
  // }

  createMarker  = (props) => {

    new window.google.maps.Marker({
      position: { lat: 43.000000, lng: -79.000000 },
      map: this.googleMap,
    })
  }
}



/*
export default class WebMap extends Component<{}, State> {
  state = {
    lat: 51.505,
    lng: -0.09,
    zoom: 13,
  }

  render() {
    const position = [this.state.lat, this.state.lng]
    return (
      <Map center={position} zoom={this.state.zoom} id="mapid">
        <TileLayer
          attribution='&amp;copy <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        />
        <Marker position={position}>
          <Popup>
            A pretty CSS3 popup. <br /> Easily customizable.
          </Popup>
        </Marker>
      </Map>
    )
  }
}
*/
