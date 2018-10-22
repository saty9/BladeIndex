var React = require('react');
var ReactDOM = require('react-dom');

class RatingTable extends React.Component{

}

class RatingRow extends React.Component{
    render () {
        return (
            <tr>
                <td>{this.props.value}</td>
                <td>{this.props.name}</td>
                <td><RatingGraph history={this.props.history}/></td>
            </tr>
        );
    }
}

class RatingGraph extends React.Component{
    render () {

    }
}

ReactDOM.render(<RatingTable />, document.getElementById("root"));