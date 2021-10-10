<template>

  <div>
    <p>Patientnamn</p>
    <!-- <PatientCard :patient="patients"/>
    <PatientCard  -->
    <div  v-if = "arr.length >= 0">
      <div v-for="(item, index) in arr" :key="item.title">
        {{item.title}}
        <a :href = "`${item.image}`" target="_blank"> {{item.image}}</a>
        <img :src="`${item.image}`" alt="">
        <v-btn @click="clear(index)">Clear</v-btn>
        <v-btn @click="add">Add</v-btn>
        
      </div>
    </div>
   
    <v-btn @click="clearAll">Clear All</v-btn>
    <v-btn @click="addAll">Add All</v-btn>
    <v-btn @click="add">Add</v-btn>
    <v-btn @click="add">Modify</v-btn>
    <!-- <v-btn @click="clear">Clear</v-btn>
    <v-btn @click="add">Add</v-btn>
    <v-btn @click="add">Modify</v-btn> -->

    <div id="example-1">
      <v-btn @click="counter += 1">Add 1</v-btn>
      <v-btn @click="counter -=1">Delete 1</v-btn>
      <p>The button above has been clicked {{ counter }} times.</p>
    </div>

  </div>

</template>

<script>
import axios from 'axios'


  export default {
    

    data(){
      return{
        patients: [],
        counter: 0,
        i : 0,
        arr:[],
        non_null:[],
      }
    },

    computed: {
      filteredList() {
        return this.postList.filter(post => {
          return post.title.toLowerCase().includes(this.search.toLowerCase())
        })
      }
    },


    methods: {
      async getData(){
         await axios.get('https://api.nuxtjs.dev/mountains').then(response =>{
          this.patients = response.data
        })

   
      
     },
     async loadFromDb() {
      const messageRef = this.$fireDb.ref('patient-info') // cases is the name of the data
      try {
        const snapshot = await messageRef.once('value')
        alert(snapshot.val().cases)
      } catch (e) {
        alert(e)
        return
        }
      },

     clear(index) {
      this.$delete(this.arr, index)
      this.i -=1
      console.log(this.i)
      
      
      },
      clearAll(){
        this.arr = []

      },

      add(){
       
        if(this.patients.length == 0){
          this.getData()
        }

        if(this.i > this.arr.length){
          this.i = this.arr.length
          console.log(this.i)
        }

        const name = this.patients[this.i]
        if (name != null && (this.arr.includes(this.name) == false)){
          this.arr.push(name)
          this.i +=1
          console.log(this.i)
          console.log(this.arr.includes(this.name))
        }
        
      },
      addAll(){
        if(this.patients.length == 0){
          this.getData()
        }
        this.arr = this.patients

      },

      async createUser() {
      try {
        await this.$fire.auth.createUserWithEmailAndPassword(
          'foo@foo.foo',
          'test'
        )
      } catch (e) {
        handleError(e)
      }
    }
 
      
    },
  }

</script>
