<template>
  <v-container>
    <v-card>
      <v-card-title>Albums</v-card-title>
      <v-card-text>
        <template>
          <v-simple-table>
            <template v-slot:default>
              <thead>
                <tr>
                  <th class="text-left">
                    id
                  </th>
                  <th class="text-left">
                    Name
                  </th>
                  <th class="text-left">
                    Artist
                  </th>
                  <th class="text-left">
                    Actions
                  </th>
                </tr>
              </thead>
              <tbody>
                <tr v-for=" (album, key) in $store.state.albums" :key="key">
                  <td width="10%">{{ album.id }}</td>
                  <td width="35%">{{ album.name }}</td>
                  <td width="35%">{{ album.artist }}</td>
                  <td> <v-btn icon small class="mr-2" @click="editAlbum(album)">
                      <v-icon>mdi-pencil</v-icon>
                    </v-btn>
                    <v-btn icon small @click="deleteAlbum(album)">
                      <v-icon>mdi-delete</v-icon>
                    </v-btn>
                  </td>
                </tr>
              </tbody>
            </template>
          </v-simple-table>
        </template>
      </v-card-text>
      <v-card-actions>
        <v-row >
          <v-col class="align-content-end">
             <v-btn color="primary" @click="openAddAlbumDialog">Agregar Album</v-btn>
          </v-col>
        </v-row>
      </v-card-actions>
    </v-card>

    <generic_dialog :dialog-visible="addAlbumDialog" :title="'Agregar Album'">
      <template #content>
        <v-text-field label="Nombre" v-model="newAlbumName" />
        <label>Escoge al artista de este album:
            <v-select flat 
            :items="options" 
            v-model="selectedValue" 
            label="Artistas" solo></v-select>
        </label>
      </template>
      <template #actions>
        <v-btn @click="addAlbum" color="blue darken-1" text>Guardar</v-btn>
        <v-btn @click="closeAddAlbumDialog" color="blue darken-1" text>Cancelar</v-btn>
      </template>
    </generic_dialog>

    <generic_dialog :dialog-visible="editAlbumDialog" :title="'Editar Album'">
      <template #content>
        <v-text-field label="Nombre" v-model="editAlbumName" />
        <label>Escoge al artista de este album:
          <v-select flat 
            :items="options" 
            v-model="selectedValue" 
            label="Artistas" solo></v-select>
        </label>
      </template>
      <template #actions>
        <v-btn @click="saveEditedAlbum" color="blue darken-1" text>Guardar</v-btn>
        <v-btn @click="closeEditAlbumDialog" color="blue darken-1" text>Cancelar</v-btn>
      </template>
    </generic_dialog>

  </v-container>
</template>

<script>

import generic_dialog from '@/components/GenericDialog.vue'

const type='albums'

export default {

  data() {
    return {
      id:1,
      newAlbumName: '',
      oldAlbum: '',
      editAlbumName: '',
      addAlbumDialog: false,
      editAlbumDialog: false,
      selectedValue:null,
      items: ''
    };
  },
  computed:{
    options(){
      return this.$store.state.artists.map(artist => artist.name)
    }
  },
  methods: {
    
    addAlbum() {
      if (this.newAlbumName) {
        const album={
          id:this.id,
          name:this.newAlbumName,
          artist:this.selectedValue
        }
        this.$store.dispatch('addAction', {type:type, newObject:album});

        this.newAlbumName = '';
        this.closeAddAlbumDialog();

        this.id++
        console.dir(JSON.stringify(album))
      }
    },
    editAlbum(album) {
      // console.log(AlbumName)
      this.oldAlbum = album;
      this.editAlbumDialog = true;
    },
    saveEditedAlbum() {
      if (this.editAlbumName||this.selectedValue) {//comprueba que se haya modificado el nombre o el artista para realizar la actualizacion
        // console.log(`${this.selectedValue} `)
        this.$store.dispatch('editAction', { type:type, oldObject: this.oldAlbum, newName: this.editAlbumName, newArtist:this.selectedValue });
        this.editAlbumName = '';
        this.closeEditAlbumDialog();
      }
    },
    deleteAlbum(album) {
      this.$store.dispatch('deleteAction', { type:type, oldObject: album });
    },
    openAddAlbumDialog() {
      this.addAlbumDialog = true;
    },
    closeAddAlbumDialog() {
      this.addAlbumDialog = false;
    },
    closeEditAlbumDialog() {
      this.editAlbumDialog = false;
    },
  },
  components: {
    generic_dialog
  }
};
</script>

<style>
v-select{
  width: 60px;
  height: 20px;
}

</style>
