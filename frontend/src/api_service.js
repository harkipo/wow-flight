import axiox from 'axios';

axiox.defaults.withCredentials = true;

const instance = axiox.create({
	baseURL: 'http://127.0.0.1:8000',
});


export class API {


    static search_flight(body) {
		const headers = {
			'Content-Type': 'application/json',
			'Access-Control-Allow-Origin': '*' 

		};
		return instance
				.post('/search-flight/', JSON.stringify(body), {
				headers: headers,
			})
			.then((resp) => resp.data);
	}



}