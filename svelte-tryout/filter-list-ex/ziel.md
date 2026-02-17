# tabelle filtern
- class Cubes im orm
- session.query().all() -> list of objects
- daraus soll eine liste generiert werden, die attribute sind die spaltennamen, und ich will  dann verschiedene spaltern filtern und sortieren
# claute ex
```js
<script>
  // ORM Query
  let cubes = $state([]);
  cubes = await session.query(Cubes).all();
  // cubes = [{id: 1, name: "Rubik", size: 3}, ...]
  
  // Filter & Sort
  let filterText = $state('');
  let sortBy = $state('name');
  
  let filtered = $derived(
    cubes
      .filter(c => c.name.includes(filterText))  // Filtern
      .sort((a, b) => a[sortBy] > b[sortBy] ? 1 : -1)  // Sortieren
  );
</script>

<!-- Tabelle -->
<input bind:value={filterText} placeholder="Filter...">
<select bind:value={sortBy}>
  <option value="name">Name</option>
  <option value="size">Size</option>
</select>

<table>
  <thead>
    <tr><th>Name</th><th>Size</th></tr>
  </thead>
  <tbody>
    {#each filtered as cube}
      <tr><td>{cube.name}</td><td>{cube.size}</td></tr>
    {/each}
  </tbody>
</table>
```
