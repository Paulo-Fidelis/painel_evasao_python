import React, { useState } from 'react';
import { View, Text, TouchableOpacity, StyleSheet, ScrollView} from 'react-native';
import { Picker } from '@react-native-picker/picker';

const alunos = [
  { id: 1, curso: "ADS", serie: "4°", turma: "B", nome: "Adriana Monteiro", presenca: 99 },
  { id: 2, curso: "TDS", serie: "1°", turma: "A", nome: "Bruno Siqueira", presenca: 79 },
  { id: 3, curso: "ADS", serie: "2°", turma: "B", nome: "Daniel Arantes", presenca: 55 },
  { id: 4, curso: "ADS", serie: "1°", turma: "A", nome: "Carla Fernandes", presenca: 82 },
  { id: 5, curso: "TDS", serie: "3°", turma: "B", nome: "Eduardo Paiva", presenca: 90 },
  { id: 6, curso: "ADS", serie: "3°", turma: "A", nome: "Fernanda Ribeiro", presenca: 96 },
  { id: 7, curso: "TDS", serie: "2°", turma: "A", nome: "Gabriel Tavares", presenca: 100 },
  { id: 8, curso: "ADS", serie: "1°", turma: "B", nome: "Helena Moura", presenca: 98 },
  { id: 9, curso: "TDS", serie: "3°", turma: "B", nome: "Igor Almeida", presenca: 85 },
  { id: 10, curso: "ADS", serie: "3°", turma: "B", nome: "Juliana Castro", presenca: 80 },
  { id: 11, curso: "TDS", serie: "2°", turma: "A", nome: "Karen Duarte", presenca: 65 },
  { id: 12, curso: "ADS", serie: "2°", turma: "A", nome: "Leonardo Pimentel", presenca: 70 },
  { id: 13, curso: "TDS", serie: "3°", turma: "A", nome: "Mariana Silveira", presenca: 25 },
  { id: 14, curso: "ADS", serie: "2°", turma: "A", nome: "Nicolas Figueiredo", presenca: 91 },
  { id: 15, curso: "ADS", serie: "3°", turma: "B", nome: "Otávia Cardoso", presenca: 85 },
  { id: 16, curso: "TDS", serie: "2°", turma: "B", nome: "Paulo Nascimento", presenca: 80 },
  { id: 17, curso: "ADS", serie: "4°", turma: "A", nome: "Quésia Araújo", presenca: 77 },
  { id: 18, curso: "TDS", serie: "1°", turma: "A", nome: "Rafael Cunha", presenca: 68 },
  { id: 19, curso: "ADS", serie: "1°", turma: "B", nome: "Sabrina Moura", presenca: 92 },
  { id: 20, curso: "TDS", serie: "3°", turma: "B", nome: "Tiago Santos", presenca: 88 },
  { id: 21, curso: "ADS", serie: "2°", turma: "A", nome: "Ursula Barros", presenca: 73 },
  { id: 22, curso: "TDS", serie: "1°", turma: "B", nome: "Victor Guedes", presenca: 95 },
  { id: 23, curso: "ADS", serie: "3°", turma: "A", nome: "Wesley Amaral", presenca: 60 },
  { id: 24, curso: "TDS", serie: "2°", turma: "A", nome: "Xavier Teles", presenca: 78 },
  { id: 25, curso: "ADS", serie: "4°", turma: "B", nome: "Yasmin Rocha", presenca: 99 },
  { id: 26, curso: "TDS", serie: "3°", turma: "A", nome: "Zeca Andrade", presenca: 55 },
  { id: 27, curso: "ADS", serie: "1°", turma: "A", nome: "Alice Martins", presenca: 84 },
  { id: 28, curso: "TDS", serie: "2°", turma: "B", nome: "Bianca Costa", presenca: 71 },
  { id: 29, curso: "ADS", serie: "3°", turma: "B", nome: "Caio Moreira", presenca: 89 },
  { id: 30, curso: "TDS", serie: "1°", turma: "A", nome: "Diego Campos", presenca: 94 },
  { id: 31, curso: "ADS", serie: "2°", turma: "A", nome: "Evelyn Duarte", presenca: 66 },
  { id: 32, curso: "TDS", serie: "4°", turma: "B", nome: "Fabiano Lopes", presenca: 74 },
  { id: 33, curso: "ADS", serie: "3°", turma: "A", nome: "Gustavo Sales", presenca: 51 },
  { id: 34, curso: "TDS", serie: "2°", turma: "A", nome: "Henrique Braga", presenca: 87 },
  { id: 35, curso: "ADS", serie: "1°", turma: "B", nome: "Isabela Vasconcelos", presenca: 98 },
  { id: 36, curso: "TDS", serie: "4°", turma: "A", nome: "Jéssica Porto", presenca: 62 },
  { id: 37, curso: "ADS", serie: "3°", turma: "A", nome: "Kauê Ribeiro", presenca: 81 },
  { id: 38, curso: "TDS", serie: "2°", turma: "B", nome: "Larissa Mendes", presenca: 93 },
  { id: 39, curso: "ADS", serie: "4°", turma: "B", nome: "Matheus Novaes", presenca: 75 },
  { id: 40, curso: "TDS", serie: "1°", turma: "B", nome: "Natália Freitas", presenca: 88 },
];


export default function HomeScreen({ navigation }) {
  const [curso, setCurso] = useState("");
  const [serie, setSerie] = useState("");
  const [turma, setTurma] = useState("");

  const filtrados = alunos.filter(a => 
    (curso === "" || a.curso === curso) &&
    (serie === "" || a.serie === serie) &&
    (turma === "" || a.turma === turma)
  );

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Alunos</Text>

      {/* FILTROS */}
      <View style={styles.filtrosLinha}>
        
        <View style={styles.filtroBox}>
          <Text style={styles.filtroLabel}>Curso:</Text>
          <View style={styles.pickerBox}>
            <Picker
              selectedValue={curso}
              onValueChange={(v) => setCurso(v)}
              style={styles.picker}
            >
              <Picker.Item label="" value="" />
              <Picker.Item label="ADS" value="ADS" />
              <Picker.Item label="TDS" value="TDS" />
            </Picker>
          </View>
        </View>

        <View style={styles.filtroBox}>
          <Text style={styles.filtroLabel}>Série/Período:</Text>
          <View style={styles.pickerBox}>
            <Picker
              selectedValue={serie}
              onValueChange={(v) => setSerie(v)}
              style={styles.picker}
            >
              <Picker.Item label="" value="" />
              <Picker.Item label="1°" value="1°" />
              <Picker.Item label="2°" value="2°" />
              <Picker.Item label="3°" value="3°" />
              <Picker.Item label="4°" value="4°" />
            </Picker>
          </View>
        </View>

        <View style={styles.filtroBox}>
          <Text style={styles.filtroLabel}>Turma:</Text>
          <View style={styles.pickerBox}>
            <Picker
              selectedValue={turma}
              onValueChange={(v) => setTurma(v)}
              style={styles.picker}
            >
              <Picker.Item label="" value="" />
              <Picker.Item label="A" value="A" />
              <Picker.Item label="B" value="B" />
            </Picker>
          </View>
        </View>

      </View>

      {/* LISTA DE ALUNOS */}
      <ScrollView style={styles.scroll} showsVerticalScrollIndicator={false}>
      {filtrados.map(a => (
        <View key={a.id} style={styles.card}>
          <Text>{a.curso} - {a.serie} - {a.turma}</Text>
          <Text style={styles.nome}>{a.nome}</Text>
          <Text style={styles.presenca}>{a.presenca}% de presença</Text>

          <TouchableOpacity onPress={() => navigation.navigate("RegistrarFalta", { id:a.id })}>
            <Text style={styles.link}>Registrar falta</Text>
          </TouchableOpacity>

          <TouchableOpacity onPress={() => navigation.navigate("ListaFaltas", { id:a.id })}>
            <Text style={styles.edit}>Editar frequência</Text>
          </TouchableOpacity>
        </View>
      ))}
      </ScrollView>
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, padding: 20, backgroundColor: "#F3E5F5" },

  title: { 
    fontSize: 28, 
    textAlign: "center", 
    marginBottom: 20,
    fontWeight: "bold",
    color: "#512DA8"
  },

  filtrosLinha: {
    flexDirection: "row",
    justifyContent: "space-between",
    marginBottom: 18
  },

  filtroBox: {
    width: "30%"
  },

  filtroLabel: {
    fontWeight: "bold",
    color: "#5E35B1",
    marginBottom: 5
  },

  pickerBox: {
    borderWidth: 2,
    borderColor: "#9575CD",
    borderRadius: 10,
    overflow: "hidden",
    backgroundColor: "#FFF"
  },

  picker: { height: 42 },

  card: {
    backgroundColor: "#fff",
    padding: 18,
    borderRadius: 16,
    marginBottom: 15,
    elevation: 5
  },

  nome: { 
    fontSize: 17, 
    fontWeight: "bold", 
    marginTop: 5,
    color: "#311B92"
  },

  presenca: { 
    color: "#555", 
    marginBottom: 10 
  },

  link: { 
    color: "#7E57C2", 
    marginBottom: 5, 
    fontWeight: "600" 
  },

  edit: { 
    color: "#512DA8", 
    fontWeight: "700" 
  }
});
