<!--<template>-->
<!--<div class="row container-fluid">-->
<!--      <div class="col-4">-->
<!--        <draggable-->
<!--        class="dragArea list-group"-->
<!--        :list="list1"-->
<!--        :group="{ name: 'people', pull: 'clone', put: false }"-->
<!--        :clone="cloneDog"-->
<!--        @change="log"-->
<!--      >-->
<!--        <div class="list-group-item" v-for="element in list1" :key="element.id">-->
<!--          {{ element.name }}-->
<!--        </div>-->
<!--      </draggable>-->
<!--      </div>-->
<!--      <div class="col-8">-->
<!--        <draggable-->
<!--        class="dragArea list-group"-->
<!--        :list="list2"-->
<!--        group="people"-->
<!--        @change="log"-->
<!--        >-->
<!--        <div class="list-group-item" v-for="element in list2" :key="element.id">-->
<!--          {{ element.name }}-->
<!--        </div>-->
<!--      </draggable>-->
<!--&lt;!&ndash;        <rawDisplayer class="col-3" :value="list1" title="List 1" />&ndash;&gt;-->
<!--&lt;!&ndash;        <rawDisplayer class="col-3" :value="list2" title="List 2" />&ndash;&gt;-->
<!--      </div>-->
<!--</div>-->
<!--</template>-->

<!--<script>-->
<!--import draggable from 'vuedraggable'-->
<!--import axios from 'axios'-->
<!--export default {-->

<!--  name: "SurveyFormBuilder",-->
<!--  data(){-->
<!--    return{-->
<!--      list1: [-->
<!--        { name: "dog 1", id: 1 },-->
<!--        { name: "dog 2", id: 2 },-->
<!--        { name: "dog 3", id: 3 },-->
<!--        { name: "dog 4", id: 4 }-->
<!--      ],-->
<!--      list2: [-->
<!--        { name: "cat 5", id: 5 },-->
<!--        { name: "cat 6", id: 6 },-->
<!--        { name: "cat 7", id: 7 }-->
<!--      ]-->
<!--    }-->
<!--  },-->
<!--  components:{-->
<!--    draggable,-->
<!--  },-->
<!--  mounted() {-->
<!--    let url = '/question-type'-->
<!--    axios.get(url)-->
<!--        .then(res=>{-->
<!--            console.log(res.data)-->
<!--            // this.list1 = res.data-->
<!--          }-->
<!--        ).catch(err=>console.log(err))-->
<!--  },-->
<!--  methods:{-->
<!--    log: function(evt) {-->
<!--      window.console.log(evt);-->
<!--    }-->
<!--  }-->
<!--}-->
<!--</script>-->


<template>
  <div class="container">
    <div class="row">
    <div class="col-4">
      <h3>Available list</h3>
      <draggable
        class="dragArea list-group"
        :list="list1"
        :group="{ name: 'people', pull: 'clone', put: false }"
        :clone="cloneDog"
        @change="log"
      >
        <div class="list-group-item" v-for="element in list1" :key="element.id">
          {{ element.title }}
        </div>
      </draggable>
    </div>

    <div class="col-8 bg-light">
      <h3>Questions</h3>
      <form @submit.prevent="submit_btn" method="POST">
      <draggable
        class="dragArea list-group"
        :list="list2"
        group="people"
        @change="log"
      >
        <div class="list-group-item border-2" v-for="(element,index) in list2" :key="element.id">
              <div class="d-flex justify-content-between mb-2">
                {{ element.title }} No {{ index+1 }}
                <span @click="removeQue(index)" class="btn btn-danger">remove</span>
              </div>
              <input :name="`question-${element.id}`" class="form-control" type="element.type">
              <div v-if ="element.type === 'radio'">
                Options
                <textarea :name="`radio-${element.id}`" class="form-control"></textarea>
              </div>
              <div v-if="element.type === 'select'" >
                <p>Options</p>
               <textarea :name="`select-${element.id}`" class="form-control"></textarea>
              </div>
              <div v-if="element.type === 'checkbox'" >
                <p>Options</p>
                <textarea :name="`checkbox-${element.id}`" class="form-control"></textarea>
              </div>
        </div>
      </draggable>
        <div class="mt-3">
          <button class="btn btn-primary" type="submit"> Save </button>
        </div>
        </form>
    </div>

  </div>
  </div>
</template>

<script>
import draggable from "vuedraggable";
import axios from 'axios'
let idGlobal = 1;
export default {
  name: "SurveyFormBuilder",
  display: "Custom Clone",
  order: 3,
  components: {
    draggable
  },
  data() {
    return {
      list1: [],
      list2: []
    };
  },
  methods: {
    submit_btn(){
      let url = '/question-type'
      let formdata = new FormData()
      formdata.set("value","test value")
      axios.post(url,formdata).then(
          res=>console.log(res.data)
      ).catch(error=>console.log(error))
    },
    log: function(evt) {
      if(evt.added)
        ++idGlobal

      // window.console.log(evt);
    },
    cloneDog({ id }) {
      return {
        id:idGlobal,
        title: `Add question?`,
        type: `${this.list1[id-1].type}`,
      };
    },
    removeQue(index){
      this.list2.splice(index,1)
    }
  },
  mounted() {
    let url = '/question-type'
    axios.get(url)
        .then(res=>{
            this.list1 = res.data
          }
        ).catch(err=>console.log(err))
  }
};
</script>