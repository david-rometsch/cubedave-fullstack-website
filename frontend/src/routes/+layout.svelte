<script>
	import './layout.css';
	import favicon from '$lib/assets/favicon.svg';

	// import '@picocss/pico/css/pico.min.css';
	// import '$static/my-style.css';
	let { children } = $props();
</script>

<h>header from layout.svelte</h>
<!-- <= here route-or-folder/+pages.svelte - content here -->
<nav class="bg-gray-900 px-6 py-3">
	<ul class="flex items-center gap-6">
		<li class="mr-auto">
			<img class="h-10 w-10 rounded-full object-cover" alt="cubes-logo" src="images/cube.jpg" />
		</li>
		<li class="cursor-pointer text-white hover:text-yellow-400">Tutorial</li>
		<li class="cursor-pointer text-white hover:text-yellow-400">Cubeshop</li>
		<li class="cursor-pointer text-white hover:text-yellow-400">3BLD</li>
	</ul>
</nav>
<!-- <nav class="navbar"> -->
<!-- 	<ul class="navbar-list"> -->
<!-- 		<li class="navbar-item navbar-left"> -->
<!-- 			<img class="navbar-img" alt="cubes-logo" src="images/cube.jpg" /> -->
<!-- 		</li> -->
<!---->
<!-- 		<li class="navbar-item">Tutorial</li> -->
<!-- 		<li class="navbar-item">Cubeshop</li> -->
<!-- 		<li class="navbar-item">3BLD</li> -->
<!-- 	</ul> -->
<!-- </nav> -->

<svelte:head>svelte:head<link rel="icon" href={favicon} /></svelte:head>
<section class="content">child here{@render children()}</section>
