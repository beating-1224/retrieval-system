<template>
  <v-container style="height:100%">
    <v-row>
      <v-col cols="10" md="5">
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
                <v-card height="200pt" width="300pt">

                  <v-container fluid>
                    <v-combobox
                        v-model="selected_datasets_1"
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
                      <v-list-item :key="item">
                        <v-list-item-content>
                          <v-row>
                            <v-col
                                v-for="it in item"
                                :key="it"
                                style="display:flex;justify-content:center;align-items:center"
                            >
                              <v-img
                                  :lazy-src="`/assets/tmp/${it}.png`"
                                  height="40"
                                  width="40"
                                  :src="`/assets/tmp/${it}.png`"
                                  contain
                                  @click="chooseSample(it)"
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
                <v-card height="200pt" width="300pt" style="display:flex;justify-content:center;align-items:center">
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
          <v-card height="250pt" width="300pt">
            <model-viewer id="reveal" loading="eager" camera-controls auto-rotate
                          poster="/assets/tmp/astronaut.png"
                          src="/assets/tmp/Astronaut.glb"
                          alt="A 3D model of a shishkebab"
            >
            </model-viewer>
          </v-card>
        </v-row>
      </v-col>

      <v-col cols="2" md="1">
        <v-card>


        </v-card>
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
                      v-model="selected_datasets_2"
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
                        v-model="checkbox1"
                        label="Point Cloud"
                    ></v-checkbox>
                  </v-col>
                  <v-col
                  >
                    <v-checkbox
                        v-model="checkbox2"
                        label="Voxel"
                    ></v-checkbox>
                  </v-col>
                  <v-col
                  >
                    <v-checkbox
                        v-model="checkbox3"
                        label="Multi-view"
                    ></v-checkbox>
                  </v-col>
                </v-row>
              </v-col>
            </v-row>
            <v-row>
              <v-virtual-scroll
                  height="480"
                  item-height="75"
                  :items="resultRows"
                  style="display:flex"
              >
                <template v-slot:default="{ item }">
                  <v-list-item :key="item">
                    <v-list-item-content>
                      <v-row style="display:flex;justify-content:center;align-items:center">
                        <v-col
                            v-for="it in item"
                            :key="it"
                            style="display:flex;justify-content:center;align-items:center"
                        >
                          <v-img
                              :lazy-src="`/assets/tmp/${it}.png`"
                              :src="`/assets/tmp/${it}.png`"
                              height="60"
                              width="60"
                              contain
                              @click="chooseResult(it)"
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
              <v-row>
                <span>
                  Object ID:
                </span>
              </v-row>

              <v-row>
                <span>
                  Name:
                </span>
              </v-row>

              <v-row>
                <span>
                  Dataset:
                </span>
              </v-row>

              <v-row>
                <span>
                  Modality:
                </span>
              </v-row>

            </v-col>
            <v-col cols="10" md="5">
              <v-tabs
                  background-color="deep-purple accent-4"
                  grow
                  dark
              >
                <v-tab key="detailTab1">Point Cloud</v-tab>
                <v-tab-item key="detailTab1" style="display:flex;justify-content:center;align-items:center">
                  <model-viewer id="detail" loading="lazy" camera-controls auto-rotate
                                poster="/assets/tmp/astronaut.png"
                                src="/assets/tmp/Astronaut.glb"
                                alt="A 3D model of a shishkebab"
                  >
                  </model-viewer>
                </v-tab-item>

                <v-tab key="detailTab2">Voxel</v-tab>
                <v-tab-item key="detailTab2" style="display:flex;justify-content:center;align-items:center">
                  <model-viewer id="detail" loading="lazy" camera-controls auto-rotate
                                poster="/assets/tmp/astronaut.png"
                                src="/assets/tmp/Astronaut.glb"
                                alt="A 3D model of a shishkebab"
                  >
                  </model-viewer>
                </v-tab-item>

                <v-tab key="detailTab3">Multi-view</v-tab>
                <v-tab-item key="detailTab3" style="display:flex;justify-content:center;align-items:center">
                  <model-viewer id="detail" loading="lazy" camera-controls auto-rotate
                                poster="/assets/tmp/astronaut.png"
                                src="/assets/tmp/Astronaut.glb"
                                alt="A 3D model of a shishkebab"
                  >
                  </model-viewer>
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

export default {
  name: "Page",
  data() {
    return {
      samples: [
        '1', '2', '3', '7', '8', '9', '1', '2', '1', '2', '3', '7', '8', '9', '1', '2','1', '2', '3', '7', '8', '9', '1', '2','1', '2', '3', '7', '8', '9', '1', '2',],
      results: [
        '8', '9', '1', '2', '3', '7', '8', '9',  '8', '9', '1', '2', '3', '7', '8', '9', '8', '9', '1', '2', '3', '7', '8', '9', '8', '9', '1', '2', '3', '7', '8', '9', '8', '9', '1', '2', '3', '7', '8', '9',],
      datasets: [
        {header: 'Select one or more datasets'},
        {
          text: 'Dataset1',
          color: 'blue',
        },
        {
          text: 'Dataset2',
          color: 'purple',
        },
        {
          text: 'Dataset3',
          color: 'indigo',
        },
        {
          text: 'Dataset4',
          color: 'cyan',
        },
      ],
      selected_datasets_1: [],
      selected_datasets_2: [],
      dialog: false,
      checkbox1: false,
      checkbox2: false,
      checkbox3: false,
    }
  },
  computed: {
    sampleRows: function () {
      let baseArray = this.samples
      let len = baseArray.length
      let n = 5
      let lineNum = len % n === 0 ? len / n : Math.floor((len / n) + 1)
      let res = []
      for (let i = 0; i < lineNum; i++) {
        let temp = baseArray.slice(i * n, i * n + n)
        res.push(temp)
      }
      return res
    },
    resultRows: function () {
      let baseArray = this.results
      let len = baseArray.length
      let n = 5
      let lineNum = len % n === 0 ? len / n : Math.floor((len / n) + 1)
      let res = []
      for (let i = 0; i < lineNum; i++) {
        let temp = baseArray.slice(i * n, i * n + n)
        res.push(temp)
      }
      return res
    }
  },
  methods: {
    chooseSample(index) {
      console.log(index)
    },
    chooseResult(index) {
      console.log(index)
      this.dialog = true
    },
  }
}
</script>

<style scoped>
model-viewer {
  width: 360px;
  height: 300px;
}

</style>