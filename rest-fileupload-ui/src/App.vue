<template>
  <div class="container pt-5">
    <div class="row">
      <div class="col-sm-4 offset-4">
        <h5 class="text-center border-bottom">Simple file upload with Django Rest and VueJs</h5>
        <div class="form mt-3">

          <div class="form-group">
            <label for="name">Name:</label>
            <input type="text" class="form-control" id="name" v-model="name" placeholder="Enter name ..">
          </div>

          <div class="form-group">
            <label>Data file:</label>
            <input type="file" class="form-control-file" ref="file" v-on:change="handleFileUpload">
          </div>

          <div class="form-group">
            <button class="btn btn-primary" v-on:click="submitFile">Submit</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

  import * as axios from 'axios';

  const BASE_URL = 'http://192.168.1.34:8000';

  export default {
    name: 'app',
    components: {},
    data() {
      return {
        name: '',
        file: ''
      }
    },
    methods: {
      handleFileUpload() {
        this.file = this.$refs.file.files[0];
      },
      submitFile() {
        let formData = new FormData();
        formData.append('name', this.name);
        formData.append('data_file', this.file);

        const url = `${BASE_URL}/create/`;
        axios
          .post(url, formData,
            {
              headers: {
                'Content-Type': 'multipart/form-data'
              }
            }
          )
          .then((data) => {
            console.log('SUCCESS!!');
            console.log(data);
          })
          .catch((error) => {
            console.log('FAILURE!!');
            console.log(error.toString());
          });
      }
    },
  }
</script>

<style scoped>
  div > button {
    width: 100%;
  }
</style>
