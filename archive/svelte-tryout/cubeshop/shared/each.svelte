<script>
	const colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'];
	let selected = $state(colors[0]);
</script>

<h1 style="color: {selected}"></h1>

<div>
		{#each colors as color}
			<button
				style="background: {color}"
				aria-label={color}
				aria-current={selected === color}
				onclick={() => selected = color}
			></button>
		{/each}
		
</div>
