<script>
	import { cubeData } from './cubes.svelte.js';
	let cubes = $state(cubeData.cubes); // gets tracked now
	let cubeType = $state('');
	const filteredCubes = $derived(cubes.filter((cube) => cube.category == cubeType));
</script>

<!-- <script> -->
<!-- 	let { children } = $props(); -->
<!-- </script> -->

<h1>Welcome to this testing page!</h1>

<h1>Cubes aus JSON</h1>

<!-- <p>{JSON.stringify(cubes, null, 2)}</p> -->
<!-- filter -->
<div>
	<button
		onclick={() => {
			cubeType = '3x3';
			console.log('3x3 clicked');
		}}>show 3x3</button
	>

	<button
		onclick={() => {
			cubeType = '4x4';
			console.log('3x3 clicked');
		}}
		>show 4x4
	</button>

	<button
		onclick={() => {
			cubeType = '2x2';
			console.log('2x2 clicked');
		}}>show 2x2</button
	>
</div>

<!-- Tabelle -->
<table border="1">
	<thead>
		<tr><th>Name</th><th>Size</th></tr>
		{#each filteredCubes as cube}
			<tr><th>{cube.name}</th><th>{cube.size}</th></tr>
		{/each}
	</thead>
	<tbody> </tbody>
</table>
