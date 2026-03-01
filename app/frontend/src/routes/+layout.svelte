<script>
	import './layout.css';
	let { children } = $props();
</script>

<nav class="bg-gray-900 px-6 py-3">
	<ul class="flex items-center gap-6">
		<li class="mr-auto">
			<a href="/">
				<img class="h-10 w-10 rounded-full object-cover" alt="cubes-logo" src="images/cube.jpg" />
			</a>
		</li>
		<li class="cursor-pointer text-white hover:text-yellow-400">Tutorial</li>
		<li class="cursor-pointer text-white hover:text-yellow-400">
			<a href="/cube-table/">Cubeshop</a>
		</li>
		<li class="cursor-pointer text-white hover:text-yellow-400">3BLD</li>
	</ul>
</nav>

<section class="content">{@render children()}</section>
