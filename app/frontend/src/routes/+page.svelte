<script>
	// import { cubeData } from './cubes.svelte.js';
	let cubeType = $state([]);
	let cubes = $state([]); // gets tracked now
	let cubeData = $state({ empty: 'none' });

	// fetch cubes from BE
	async function getAllCubes() {
		let responseJson = '';
		try {
			let response = await fetch('http://127.0.0.1:8000/api/all_cubes');
			if (!response.ok) throw new Error(`HTTP Fehler! Status: ${response.status}`);
			responseJson = await response.json();
			cubes = responseJson.cubes;
			cubes = JSON.stringify(responseJson, null, 2);
			console.log('cubes: ', cubes); // output.textContent = JSON.stringify(data, null, 2)
		} catch (err) {
			// output.textContent = "Fehler: " + err.message
			console.error('Fetch-Fehler:', err);
		}
		// console.log("response: ", responseJson);
		// cubeData = responseJson;
	}
	getAllCubes();

	// console.log("cube-data: ", cubeData);
	const filteredCubes = $derived(cubes.filter((cube) => cube.category == cubeType));
</script>

<h1>hello from +page.svelte from src/ i am the index!</h1>
<p>Visit <a href="https://svelte.dev/docs/kit">svelte.dev/docs/kit</a> to read the documentation</p>
