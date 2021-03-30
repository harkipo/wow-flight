import React, { useState } from 'react';
import { API } from '../api_service';



function FlightSearch() {

	const [departure_city , set_departure_city] = useState('');
	const [arrival_city , set_arrival_city] = useState('');	
	const [departure_time , set_departure_time] = useState('');	
	const [direct_flight_plans , set_direct_flight_plans] = useState([]);	
	const [connecting_flight_plans , set_connecting_flight_plans] = useState([]);	


	const search_btn_click = (e) => {
		e.preventDefault();

		console.log("Search button clicked");

		API.search_flight({departure_city,arrival_city,departure_time})
			.then(resp => {
				// set_flight_plans(resp)
				const new_direct_arr = [...resp.direct_flight_plans]
				const new_connecting_arr = [...resp.connecting_flight_plans]
				set_direct_flight_plans(new_direct_arr)
				set_connecting_flight_plans(new_connecting_arr)
				
			})
			.catch(error => {
				console.log(error);
				
			})

		
	}


    return(
        <div className="container">

		  
		<section className="search_section">
		<div>
					<h1 className="text-center">
						Flight Search App
					</h1>
				</div>
                
				<br></br>
				<br></br>
				<div className="row form-group">

						<div className="col col-md-4">
							<input type="text" className="form-control" onChange={(event) => set_departure_city(event.target.value)} placeholder="Departure City"></input>
						</div>
						<div className="col col-md-4">
							<input type="text" className="form-control" onChange={(event) => set_arrival_city(event.target.value)} placeholder="Arrival City"></input>
						</div>
						<div className="col col-md-4">
							<input type="datetime-local" className="form-control" onChange={(event) => set_departure_time(event.target.value)} placeholder="Departure Time"></input>
						</div>
          		</div>
				<br></br>

				  <div>
				  <button className="btn btn-primary" onClick={search_btn_click} type="button">Search</button>
				  </div>
				  <br></br>
				<br></br>
				</section>

		 		
				
				<br></br>
				<br></br>



                { (direct_flight_plans.length !== 0 && connecting_flight_plans.length !== 0) ? <section className="result_section"> 
		<div className="direct_flight_div">
			  <h3 align="left"> Direct flights</h3>
				<br></br>

			  {direct_flight_plans.map(flight => 

			  <div style={{border: '.5px solid black',borderRadius: '50px'}}>
				<div className="row">
					<div className="col col-md-4">
						<h4> flight number</h4>
						<h5> {flight.number} </h5>

					</div>
					<div className="col col-md-4">
						<h4> from</h4>
						<h5> {flight.departure_city} </h5>

					</div>
					<div className="col col-md-4">
						<h4> to</h4>
						<h5> {flight.arrival_city} </h5>

					</div>

				</div>
			</div>
			  
			 
			 )}

			</div>

			<br></br>


			  <div className="connecting_flight_div">

					<h3 align="left"> connecting flights  </h3>
					<br></br>
					{connecting_flight_plans.map(flight => 
						<div>
							<div style={{border: '.5px solid black',borderRadius: '50px'}}>
							<div className="row">
								<div className="col col-md-4">
									<h4> flight number</h4>
									<h5> {flight.first_number} </h5>

								</div>
								<div className="col col-md-4">
									<h4> from</h4>
									<h5> {flight.first_departure_city} </h5>

								</div>
								<div className="col col-md-4">
									<h4> to</h4>
									<h5> {flight.first_arrival_city} </h5>

								</div>

							</div>
							</div>
							<br></br>

							<div style={{border: '.5px solid black',borderRadius: '50px'}}>
							<div className="row">
								<div className="col col-md-4">
									<h4> flight number</h4>
									<h5> {flight.second_number} </h5>

								</div>
								<div className="col col-md-4">
									<h4> from</h4>
									<h5> {flight.second_departure_city} </h5>

								</div>
								<div className="col col-md-4">
									<h4> to</h4>
									<h5> {flight.second_arrival_city} </h5>

								</div>

							</div>
							</div>

							<br></br>
							<br></br>
							<br></br>
						</div>

						
					



						)}
				</div>

		</section>
 : <div></div> }

		
		 
		
	


	
      </div>
    );

}
export default FlightSearch;
