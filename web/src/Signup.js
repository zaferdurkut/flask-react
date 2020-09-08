import Container from "react-bootstrap/Container";
import Jumbotron from "react-bootstrap/Jumbotron";
import React from "react";
import Button from "react-bootstrap/Button";
import Form from "reactstrap/es/Form";
import FormGroup from "react-bootstrap/FormGroup";
import Col from "react-bootstrap/Col";
import Label from "reactstrap/es/Label";
import Input from "reactstrap/es/Input";


export default class NameForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {first_name: '', last_name: '', email: '', address: ''};
    }

    handleChange = (event) => {
        this.setState({[event.target.name]: event.target.value});
    }

    handleSubmit = (event) => {
        fetch("http://localhost:1996/api/brokers/", {
                method: "POST",
                cache: "no-cache",
                headers: {
                    "content_type": "application/json",
                },
                body: JSON.stringify(this.state)
            }
        ).then(response => {

          console.log(response)
        })
            .then(json => {

                console.log(json)
            })

        event.preventDefault();
    };

    render() {
        return (


            <Container className="p-6">

                <Jumbotron>

                    <Form className="form" onSubmit={this.handleSubmit}>
                        <Col>
                            <FormGroup>
                                <Label>First Name</Label>
                                <Input
                                    type="text"
                                    name="first_name"
                                    id="first_name"
                                    placeholder="First Name"
                                    required
                                    onChange={this.handleChange}

                                />
                            </FormGroup>
                        </Col>
                        <Col>
                            <FormGroup>
                                <Label>Last Name</Label>
                                <Input
                                    type="text"
                                    name="last_name"
                                    id="last_name"
                                    placeholder="Last Name"
                                    required
                                    onChange={this.handleChange}

                                />
                            </FormGroup>
                        </Col>
                        <Col>
                            <FormGroup>
                                <Label>Email</Label>
                                <Input
                                    type="email"
                                    name="email"
                                    id="email"
                                    placeholder="Email"
                                    onChange={this.handleChange}

                                />
                            </FormGroup>
                        </Col>
                        <Col>
                            <FormGroup>
                                <Label>Address</Label>
                                <Input
                                    type="text"
                                    name="address"
                                    id="address"
                                    placeholder="Address"
                                    required
                                    onChange={this.handleChange}
                                />
                            </FormGroup>
                        </Col>


                        <Button type="submit">Submit</Button>
                    </Form>

                </Jumbotron>
            </Container>


        );
    }
}
