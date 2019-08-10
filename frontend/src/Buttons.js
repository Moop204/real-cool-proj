import React, { Component } from 'react'
import {Button, Grid, Segment, Input, Form } from 'semantic-ui-react'

export default class SubmitButton extends Component {
    constructor(props) {
        super(props)
        this.state = {value: "Search"}
    }

    handleSubmit = () => {
        console.log("oh godf fuck fuck")
        fetch('localhost:5000/main', {
            method:"POST",
            mode: 'no-cors', 
            cache: 'no-cache', 
            credentials: 'same-origin',
            headers: {
              'Content-Type':'application/json',
            }, 
            redirect: 'follow', 
            referrer: 'no-referrer', 
            body: JSON.stringify({'place':`${this.state.value}`})  
          }
        )
        .then(response=>{
            console.log(response)
            return response
        })
        .catch(function(error) {
            console.log(error)
        })
    }

    handleChange = (event) => {
        console.log("asdfasdf")
        this.setState({value: event.target.value})
        console.log(event.target.value)
    }

    render() {
        return (
            <Form onSubmit={this.handleSubmit}>
                <Form.Field>
                    <input content="Search" value={this.state.value} onChange={this.handleChange}/>
                </Form.Field>
                <Form.Button/>
            </Form>

        )
    }
}