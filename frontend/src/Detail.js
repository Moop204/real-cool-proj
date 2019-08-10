import React from 'react'
import { Input, Container, Segment } from 'semantic-ui-react'
const InputFocus = () => (
  <Input focus placeholder='Search...' />
);

const actionbar = () => (
  <Container>
    <Segment attached='top'>DETAILS</Segment>
    <Segment>SAMPLE</Segment>
    <InputFocus />
  </Container>
)

const getToApi = (place) => {
  fetch('localhost:5000/main', {
    method:"POST",
    mode: 'cors', 
    cache: 'no-cache', 
    credentials: 'same-origin',
    headers: {
      'Content-Type':'application/json',
    }, 
    redirect: 'follow', 
    referrer: 'no-referrer', 
    body: JSON.stringify({'place':`${place}`})  
  })
  .then(response=>response.json())
}




export default actionbar 
