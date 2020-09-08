import BootstrapTable from "react-bootstrap-table-next";
import Container from "react-bootstrap/Container";
import Jumbotron from "react-bootstrap/Jumbotron";
import React from "react";



const columns = [
    {
        dataField: "id",
        text: "Product ID",
        sort: true
    },
        {
        dataField: "agency_id",
        text: "Agency ID",
        sort: true
    },
    {
        dataField: "first_name",
        text: "Firstname"
    },
    {
        dataField: "last_name",
        text: "Lastname"
    },
    {
        dataField: "email",
        text: "Email"
    },
    {
        dataField: "address",
        text: "Address"
    }
];

export default class Brokers extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            error: null,
            isLoaded: false,
            items: []
        };
    }

    componentDidMount() {
        fetch("http://localhost:1996/api/brokers/")
            .then(res => res.json())
            .then(
                (result) => {
                    this.setState({
                        isLoaded: true,
                        items: result
                    });
                },

                (error) => {
                    this.setState({
                        isLoaded: true,
                        error
                    });
                }
            )
    }

    render() {

        const {error, isLoaded, items} = this.state;
        if (error) {
            return <Container className="p-6">

                <Jumbotron>
                    <h2 className="headertekst">Brokers</h2>
                    <div className="App">
                        <div>Error: {error.message}</div>
                    </div>
                </Jumbotron>

            </Container>;
        } else if (!isLoaded) {

            return <Container className="p-6">

                <Jumbotron>
                    <h2 className="headertekst">Brokers</h2>
                    <div className="App">
                        <div>Loading...</div>
                    </div>
                </Jumbotron>

            </Container>;


        } else {
            return (
                <Container className="p-6">

                    <Jumbotron>
                        <h2 className="headertekst">Brokers</h2>

                        <div className="App">
                            <BootstrapTable
                                bootstrap4
                                keyField="id"
                                data={items}
                                columns={columns}
                            />
                        </div>
                    </Jumbotron>


                </Container>
            );
        }
    }
}



