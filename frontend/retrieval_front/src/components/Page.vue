<template>
  <v-container style="height:100%">
    <v-row>
      <v-col cols="12" md="6">
        <v-row>
          <v-card>
            <v-card-title class="justify-center">Query</v-card-title>
            <v-tabs
                background-color="deep-purple accent-4"
                grow
                dark
            >
              <v-tab key="tab1">Samples</v-tab>
              <v-tab-item key="tab1">
                <v-card height="200pt" width="400pt">

                  <v-container fluid>
                    <v-combobox
                        v-model="sampleDatasets"
                        v-on:change="sampleDatasetsChanged"
                        :items="datasets"
                        hide-selected
                        label="Search for datasets"
                        multiple
                        small-chips
                        solo
                        hide-details
                    >
                      <template v-slot:selection="{ attrs, item, parent, selected }">
                        <v-chip
                            v-if="item === Object(item)"
                            v-bind="attrs"
                            :color="`${item.color} lighten-3`"
                            :input-value="selected"
                            label
                            small
                        >
                          <span class="pr-2">
                            {{ item.text }}
                          </span>
                          <v-icon
                              small
                              @click="parent.selectItem(item)"
                          >
                            $delete
                          </v-icon>
                        </v-chip>
                      </template>
                      <template v-slot:item="{ index, item }">
                        <v-chip
                            :color="`${item.color} lighten-3`"
                            dark
                            label
                            small
                        >
                          {{ item.text }}
                        </v-chip>
                        <v-spacer></v-spacer>
                      </template>
                    </v-combobox>
                  </v-container>

                  <v-virtual-scroll
                      height="180"
                      item-height="50"
                      :items="sampleRows"
                  >
                    <template v-slot:default="{ item }">
                      <v-list-item :key="item.id">
                        <v-list-item-content>
                          <v-row>
                            <v-col
                                v-for="it in item.arr"
                                :key="it.id"
                                style="display:flex;justify-content:center;align-items:center"
                            >
                              <v-img
                                  :lazy-src="`http://127.0.0.1:8888/${it.path}`"
                                  height="40"
                                  width="40"
                                  :src="`http://127.0.0.1:8888/${it.path}`"
                                  contain
                                  @click="chooseSample(it.path)"
                                  style="border: 1px solid lightgray;"
                              ></v-img>
                            </v-col>
                          </v-row>
                        </v-list-item-content>
                      </v-list-item>
                    </template>
                    <v-divider></v-divider>

                  </v-virtual-scroll>
                </v-card>
              </v-tab-item>
              <v-tab key="tab2">Upload</v-tab>
              <v-tab-item key="tab2">
                <v-card height="200pt" width="400pt" style="display:flex;justify-content:center;align-items:center">
                  <v-btn
                      depressed
                      color="primary"
                  >
                    Upload File
                  </v-btn>
                </v-card>
              </v-tab-item>
            </v-tabs>
          </v-card>
        </v-row>

        <v-row>
          <v-card height="250pt" width="400pt">
            <v-row style="margin:0">
              <v-col cols="9">
                <!--                <model-viewer id="reveal" loading="eager" camera-controls auto-rotate-->
                <!--                              poster="/assets/tmp/astronaut.png"-->
                <!--                              src="/assets/tmp/Astronaut.glb"-->
                <!--                              alt="A 3D model of a shishkebab"-->
                <!--                >-->
                <!--                </model-viewer>-->
                <v-img
                    :lazy-src="`http://127.0.0.1:8888/${showedSample}`"
                    height="320"
                    width="360"
                    :src="`http://127.0.0.1:8888/${showedSample}`"
                    contain
                    style="border: 1px solid lightgray;"
                >
                </v-img>
              </v-col>
              <!--              <v-col cols="3" style="display:flex;align-items:flex-end;">-->
              <v-col cols="3">
                <v-row style="display:flex;justify-content:center;align-items:center;margin:12px">
                  <v-btn
                      color="deep-purple accent-4"
                      dark
                      @click="beginSearch"
                  >
                    Search
                  </v-btn>
                </v-row>

                <v-row style="display:flex;justify-content:center;align-items:center;margin:0">
                  <v-card>
                    <v-list two-line>
                      <v-list-item>
                        <v-list-item-content>
                          <v-list-item-title v-html="`Dataset`"></v-list-item-title>
                          <v-list-item-subtitle v-html="showedSampleDataset"></v-list-item-subtitle>
                        </v-list-item-content>
                      </v-list-item>
                      <v-divider
                      ></v-divider>
                      <v-list-item>
                        <v-list-item-content>
                          <v-list-item-title v-html="`Label`"></v-list-item-title>
                          <v-list-item-subtitle v-html="showedSampleLabel"></v-list-item-subtitle>
                        </v-list-item-content>
                      </v-list-item>
                      <v-divider
                      ></v-divider>
                      <v-list-item>
                        <v-list-item-content>
                          <v-list-item-title v-html="`Modality`"></v-list-item-title>
                          <v-list-item-subtitle v-html="showedSampleModality"></v-list-item-subtitle>
                        </v-list-item-content>
                      </v-list-item>
                    </v-list>
                  </v-card>
                </v-row>

              </v-col>
            </v-row>
          </v-card>

        </v-row>
      </v-col>

      <v-col cols="12" md="6">
        <v-row>
          <v-card width="600pt">
            <v-card-title class="justify-center">Target Pools</v-card-title>
            <v-row>
              <v-col cols="2" style="min-width:100pt;display:flex;justify-content:center;align-items:center"
              >
                <v-chip
                    class="ma-2"
                    color="deep-purple accent-4"
                    dark
                    label
                >
                  DATASET
                </v-chip>
              </v-col>
              <v-col>
                <v-container fluid>
                  <v-combobox
                      v-model="resultDatasets"
                      v-on:change="resultDatasetsChanged"
                      :items="datasets"
                      hide-selected
                      label="Search for datasets"
                      multiple
                      small-chips
                      solo
                      hide-details
                  >
                    <template v-slot:selection="{ attrs, item, parent, selected }">
                      <v-chip
                          v-if="item === Object(item)"
                          v-bind="attrs"
                          :color="`${item.color} lighten-3`"
                          :input-value="selected"
                          label
                          small
                      >
                          <span class="pr-2">
                            {{ item.text }}
                          </span>
                        <v-icon
                            small
                            @click="parent.selectItem(item)"
                        >
                          $delete
                        </v-icon>
                      </v-chip>
                    </template>
                    <template v-slot:item="{ index, item }">
                      <v-chip
                          :color="`${item.color} lighten-3`"
                          dark
                          label
                          small
                      >
                        {{ item.text }}
                      </v-chip>
                      <v-spacer></v-spacer>
                    </template>
                  </v-combobox>
                </v-container>
              </v-col>
            </v-row>
            <v-row>
              <v-col cols="2" style="min-width:100pt;display:flex;justify-content:center;align-items:center"
              >
                <v-chip
                    class="ma-2"
                    color="deep-purple accent-4"
                    dark
                    label
                >
                  MODALITY
                </v-chip>
              </v-col>
              <v-col
              >
                <v-row>
                  <v-col
                  >
                    <v-checkbox
                        v-model="targetModality[0]"
                        label="Point Cloud"
                        color="deep-purple accent-4"
                    ></v-checkbox>
                  </v-col>
                  <v-col
                  >
                    <v-checkbox
                        v-model="targetModality[1]"
                        label="Voxel"
                        color="deep-purple accent-4"
                    ></v-checkbox>
                  </v-col>
                  <v-col
                  >
                    <v-checkbox
                        v-model="targetModality[2]"
                        label="Multi-view"
                        color="deep-purple accent-4"
                    ></v-checkbox>
                  </v-col>
                </v-row>
              </v-col>
            </v-row>
            <v-row style="margin: 0">
              <v-virtual-scroll
                  height="480"
                  item-height="75"
                  :items="resultRows"
                  style="display:flex"
              >
                <template v-slot:default="{ item }">
                  <v-list-item :key="item.id">
                    <v-list-item-content>
                      <v-row style="display:flex;justify-content:center;align-items:center">
                        <v-col
                            v-for="it in item.arr"
                            :key="it.id"
                            style="display:flex;justify-content:center;align-items:center"
                        >
                          <v-img
                              :lazy-src="`http://127.0.0.1:8888/${it.path}`"
                              :src="`http://127.0.0.1:8888/${it.path}`"
                              height="55"
                              width="55"
                              contain
                              @click="chooseResult(it.path)"
                              style="border: 1px solid lightgray;"
                          ></v-img>
                        </v-col>
                      </v-row>
                    </v-list-item-content>
                  </v-list-item>
                </template>
                <v-divider></v-divider>

              </v-virtual-scroll>
            </v-row>

          </v-card>
        </v-row>

        <v-row>
        </v-row>
      </v-col>
    </v-row>
    <div class="text-center">
      <v-dialog
          v-model="dialog"
          height="600"
      >
        <v-card>
          <v-card-title class="text-h5 grey lighten-2">
            Object Detail
          </v-card-title>

          <v-row style="display:flex;justify-content:center;align-items:center">
            <v-col cols="10" md="5">
              <v-list two-line>
                <v-list-item>
                  <v-list-item-content>
                    <v-list-item-title v-html="`Dataset`"></v-list-item-title>
                    <v-list-item-subtitle v-html="showedSampleDataset"></v-list-item-subtitle>
                  </v-list-item-content>
                </v-list-item>
                <v-divider
                ></v-divider>
                <v-list-item>
                  <v-list-item-content>
                    <v-list-item-title v-html="`Label`"></v-list-item-title>
                    <v-list-item-subtitle v-html="showedSampleLabel"></v-list-item-subtitle>
                  </v-list-item-content>
                </v-list-item>
                <v-divider
                ></v-divider>
                <v-list-item>
                  <v-list-item-content>
                    <v-list-item-title v-html="`Object ID`"></v-list-item-title>
                    <v-list-item-subtitle v-html="details['objectId']"></v-list-item-subtitle>
                  </v-list-item-content>
                </v-list-item>
              </v-list>

            </v-col>
            <v-col cols="10" md="5">
              <v-tabs
                  background-color="deep-purple accent-4"
                  grow
                  dark
              >
                <v-tab key="detailTab1">Point Cloud</v-tab>
                <v-tab-item key="detailTab1" style="margin-left:auto; margin-right:auto">
                  <!--                  <model-viewer id="detail1" loading="lazy" camera-controls auto-rotate-->
                  <!--                                poster="/assets/tmp/astronaut.png"-->
                  <!--                                src="/assets/tmp/Astronaut.glb"-->
                  <!--                                alt="A 3D model of a shishkebab"-->
                  <!--                  >-->
                  <!--                  </model-viewer>-->
                  <v-img
                      :lazy-src="`http://127.0.0.1:8888/${details.pt}`"
                      height="320"
                      width="360"
                      :src="`http://127.0.0.1:8888/${details.pt}`"
                      contain
                      style="border: 1px solid lightgray;"
                  >
                  </v-img>
                </v-tab-item>

                <v-tab key="detailTab2">Voxel</v-tab>
                <v-tab-item key="detailTab2" style="margin-left:auto; margin-right:auto">
                  <!--                  <model-viewer id="detail2" loading="lazy" camera-controls auto-rotate-->
                  <!--                                poster="/assets/tmp/astronaut.png"-->
                  <!--                                src="/assets/tmp/Astronaut.glb"-->
                  <!--                                alt="A 3D model of a shishkebab"-->
                  <!--                  >-->
                  <!--                  </model-viewer>-->
                  <v-img
                      :lazy-src="`http://127.0.0.1:8888/${details.vx}`"
                      height="320"
                      width="360"
                      :src="`http://127.0.0.1:8888/${details.vx}`"
                      contain
                      style="border: 1px solid lightgray;"
                  >
                  </v-img>
                </v-tab-item>

                <v-tab key="detailTab3">Multi-view</v-tab>
                <v-tab-item key="detailTab3" style="margin-left:auto; margin-right:auto">
                  <!--                  <model-viewer id="detail3" loading="lazy" camera-controls auto-rotate-->
                  <!--                                poster="/assets/tmp/astronaut.png"-->
                  <!--                                src="/assets/tmp/Astronaut.glb"-->
                  <!--                                alt="A 3D model of a shishkebab"-->
                  <!--                  >-->
                  <!--                  </model-viewer>-->
                  <v-img
                      :lazy-src="`http://127.0.0.1:8888/${details.mv}`"
                      height="320"
                      width="360"
                      :src="`http://127.0.0.1:8888/${details.mv}`"
                      contain
                      style="border: 1px solid lightgray;"
                  >
                  </v-img>
                </v-tab-item>
              </v-tabs>
            </v-col>
          </v-row>


          <v-divider></v-divider>

          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn
                color="deep-purple accent-4"
                dark
                text
                @click="dialog = false"
            >
              Close
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </div>
  </v-container>

</template>

<script>
import api from "../api"

export default {
  name: "Page",
  data() {
    return {
      samples: [],
      results: [],
      datasets: [
        {header: 'Select one or more datasets'},
      ],
      colors: ['blue', 'purple', 'indigo', 'cyan', 'red', 'pink'],
      sampleDatasets: [],
      resultDatasets: [],
      dialog: false,
      targetModality: [false, false, false],
      showedSample: '',
      details: {
        'pt': '',
        'vx': '',
        'mv': '',
        'objectId': '',
        'label': ''
      },
    }
  },
  mounted: function () {
    this.getDatasets()
    // this.chooseSample(this.samples[0])
  },
  computed: {
    sampleRows: function () {
      let baseArray = []
      for (let i = 0; i < this.samples.length; i++) {
        baseArray.push({'path': this.samples[i], 'id': i})
      }
      let len = baseArray.length
      let n = 5
      let lineNum = len % n === 0 ? len / n : Math.floor((len / n) + 1)
      let res = []
      for (let i = 0; i < lineNum; i++) {
        let temp = baseArray.slice(i * n, i * n + n)
        res.push({'arr': temp, 'row': i})
      }
      return res
    },
    resultRows: function () {
      let baseArray = []
      for (let i = 0; i < this.results.length; i++) {
        baseArray.push({'path': this.results[i], 'id': i})
      }
      let len = baseArray.length
      let n = 5
      let lineNum = len % n === 0 ? len / n : Math.floor((len / n) + 1)
      let res = []
      for (let i = 0; i < lineNum; i++) {
        let temp = baseArray.slice(i * n, i * n + n)
        res.push({'arr': temp, 'row': i})
      }
      return res
    },
    showedSampleDataset: function () {
      return this.showedSample.split('/')[1]
    },
    showedSampleLabel: function () {
      return this.showedSample.split('/')[2]
    },
    showedSampleModality: function () {
      let file = this.showedSample.split('/')[4]
      if (file === undefined) {
        return '        '
      }
      let m = file.split('.')[0]
      if (m === 'pt') {
        return 'Point Cloud'
      }
      if (m === 'vox') {
        return 'Voxel'
      }
      if (m === 'mv') {
        return 'Multi-view'
      }
      return ''
    },
  },
  methods: {
    chooseSample(index) {
      this.showedSample = index
    }
    ,
    chooseResult(index) {
      this.dialog = true
      api.getDetails(index)
          .then(res => {
            if (res.status === 200) {
              this.details['pt'] = res.data['pt']
              this.details['vx'] = res.data['vx']
              this.details['mv'] = res.data['mv']
              this.details['objectId'] = res.data['objectId']
              this.details['label'] = res.data['label']
            }
            console.log(this.details)
          })
          .catch(error => {
            console.log(error)
          })
    }
    ,
    beginSearch() {
      let resultDatasets = []
      for (let i = 0; i < this.resultDatasets.length; i++) {
        resultDatasets.push(this.resultDatasets[i].text)
      }
      let datasets = ''
      for (let i = 0; i < this.resultDatasets.length; i++) {
        datasets += this.resultDatasets[i].text
        datasets += ','
      }


      let modalities = ''
      if (this.targetModality[0]) {
        modalities += 'pt,'
      }
      if (this.targetModality[1]) {
        modalities += 'vx,'
      }
      if (this.targetModality[2]) {
        modalities += 'mv,'
      }
      api.search(this.showedSample, datasets, modalities)
          .then(res => {
            if (res.status === 200) {
              this.results = res.data['results']
            }
          })
          .catch(error => {
            console.log(error)
          })
    }
    ,
    getDatasets() {
      api.getDatasets()
          .then(res => {
            if (res.status === 200) {
              let datasets = res.data['datasets']
              for (let j = 0; j < datasets.length; j++) {
                this.datasets.push({
                  text: datasets[j],
                  color: this.colors[j % (this.colors.length)]
                })
              }
              if (this.datasets.length > 1) {
                this.sampleDatasets.push(this.datasets[1])
                this.sampleDatasetsChanged()
              }
            }
          })
          .catch(error => {
            console.log(error)
          })
    }
    ,
    sampleDatasetsChanged() {
      // this.sampleDatasets
      let datasets = ''
      for (let i = 0; i < this.sampleDatasets.length; i++) {
        datasets += this.sampleDatasets[i].text
        datasets += ','
      }
      api.getSamples(datasets)
          .then(res => {
            if (res.status === 200) {
              let samples = res.data['samples']
              this.samples = samples
              this.chooseSample(this.samples[0])
            }
          })
          .catch(error => {
            console.log(error)
          })
    },
    resultDatasetsChanged() {

    }
  }
  ,

}
</script>

<style scoped>
model-viewer {
  width: 360px;
  height: 300px;
}

</style>