<template>
  <div class="hello">
    <img :src="image_url" style="width:40%;">
    <p>{{ description }}</p>
    <h2>{{ brand }}</h2>
    <div class= "row">
    <div class= "col-4">
      <div id= "HelloWorld">
      <ul class='list-group' v-for="(value, key) in info">
        <li class="list-group-item">{{ key }}</li>
      
      </ul>
      </div>
      </div>
    </div>

 
  <div class="alert alert-success alert-dismissible fade show" role="alert">
  With Bootstrap!
  <button type="button" class="close" data-dismiss="alert" aria-label="Close">
    <span aria-hidden="true">&times;</span>
  </button>
  </div>
  </div>
  
</template>

<script>
import axios from 'axios';
export default {
  name: 'HelloWorld',
  data () {
    return {
      url: 'https://www.ah.nl/producten/product/wi104392/ah-zaanlander-jong-48-plakken',
      id: 'wi104392',
      brand: 'AH Zaanlander',
      image_url: 'https://static.ah.nl/static/product/AHI_43545239363738303831_1_LowRes_JPG.JPG',
      description: 'AH Zaanlander Jong 48+ plakken',
      info: null,
      test : 'test'
    }
  }, 
  mounted (){
      axios
      .get('https://dog.ceo/api/breeds/list/all')
      .then(response => (this.info = response.data.message)) 
  }  
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
