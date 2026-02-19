<script>
	import favicon from '$lib/assets/favicon.svg';
	// import '@picocss/pico/css/pico.min.css';
	// import '../my-style.css';
	let { children } = $props();
</script>

<h>header from layout.svelte</h>

<!-- <= here route-or-folder/+pages.svelte - content here -->

<nav class="navbar">
	<ul class="navbar-list">
		<li class="navbar-item navbar-left">
			<img class="navbar-img" alt="cubes-logo" src="images/cube.jpg" />
		</li>
		<li class="navbar-item">Tutorial</li>
		<li class="navbar-item">Cubeshop</li>
		<li class="navbar-item">3BLD</li>
	</ul>
</nav>
<section class="content">
	{@render children()}
</section>

<svelte:head>
	<link rel="icon" href={favicon} />
</svelte:head>
