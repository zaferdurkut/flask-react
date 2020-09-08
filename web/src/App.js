import React from 'react';
import {MemoryRouter, Switch, Route} from 'react-router-dom';
import './App.css';
import Brokers from './Brokers.js';


import Jumbotron from 'react-bootstrap/Jumbotron';
import Container from 'react-bootstrap/Container';
import Button from 'react-bootstrap/Button';
import ButtonToolbar from 'react-bootstrap/ButtonToolbar';
import {LinkContainer} from 'react-router-bootstrap';
import "bootstrap/dist/css/bootstrap.css";
import "react-bootstrap-table-next/dist/react-bootstrap-table2.min.css";

import Navbar from "react-bootstrap/Navbar";
import Nav from "react-bootstrap/Nav";


const OurNav = () => (
    <Switch>

        <Navbar bg="light" expand="lg">
            <Navbar.Brand href="#home">Flask - React</Navbar.Brand>
            <Navbar.Collapse id="basic-navbar-nav">
                <Nav className="mr-auto">
                    <Nav.Link to="/">Home</Nav.Link>
                    {/*<Nav.Link to="/brokers" component={Brokers}>Brokers</Nav.Link>*/}
                    {/*<Nav.Link href="/agencies" component={Agencies}>Agencies</Nav.Link>*/}
                    {/*<Nav.Link href="/agencies-domain-hitelist" component={AgenciesDomainWhitelist}>Agencies Domain*/}
                    {/*    Whitelist</Nav.Link>*/}

                </Nav>
            </Navbar.Collapse>
        </Navbar>
    </Switch>
);



const Agencies = () => <span>bro</span>;

const AgenciesDomainWhitelist = () => <span>nbr</span>;


export default function App() {

    return (<MemoryRouter>

            <OurNav/>

            <Container className="p-6">

                <Jumbotron>
                    <h2>
                        <Switch>
                            <Route path="/about">
                                <Brokers/>
                            </Route>

                            <Route path="/users">
                                <Agencies/>
                            </Route>

                            <Route path="/">
                                <AgenciesDomainWhitelist/>
                            </Route>
                        </Switch>

                    </h2>


                    <h2>
                        <ButtonToolbar className="custom-btn-toolbar">
                            <LinkContainer to="/">
                                <Button>Home</Button>
                            </LinkContainer>
                            <LinkContainer to="/about">
                                <Button>About</Button>
                            </LinkContainer>
                            <LinkContainer to="/users">
                                <Button>Users</Button>
                            </LinkContainer>
                        </ButtonToolbar>
                    </h2>

                </Jumbotron>
            </Container>

            <Brokers/>

        </MemoryRouter>
    );
}

