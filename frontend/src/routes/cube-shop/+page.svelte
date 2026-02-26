<!-- <script> -->
<!-- 	let { children } = $props(); -->
<!-- </script> -->

<h1>Welcome to the cubeshop!</h1>
<div class="container">
	<div class="row">
		<div class="col-md-4 item">
			<!-- <img src="{{ url_for('static', filename='images/' ~ cube['img'] ~ '.jpg') }}" alt="{{cube['name']}}" class="img-fluid"> -->
			<table class="table-spacing">
				<thead>
					<tr>
						<th> <img class="cube" alt="cubes-logo" src="images/cube.jpg" /> </th>
						<!-- <img src="/images/cube.jpg" alt="cube-image"><cube-image></img> -->
						<td class="table-cells">name</td>
						<!-- <td class="table-cells">{{cube.name}}</td> -->
						<td class="table-cells">Preis</td>
						<!-- <td class="table-cells">{{cube.price}}</td> -->
					</tr>
				</thead>
			</table>
		</div>
	</div>
</div>
