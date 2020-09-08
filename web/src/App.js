import React from 'react';
import {MemoryRouter, Switch} from 'react-router-dom';
import './App.css';
import Agencies from './Agencies.js';
import AgencyDomainWhitelist from './AgencyDomainWhiteList';
import Brokers from './Brokers.js';
import NameForm from './Signup.js';
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


export default function App() {

    return (
        <MemoryRouter>

            <OurNav/>
            <NameForm/>
            <Brokers/>
            <Agencies/>
            <AgencyDomainWhitelist/>


        </MemoryRouter>
    );
}

