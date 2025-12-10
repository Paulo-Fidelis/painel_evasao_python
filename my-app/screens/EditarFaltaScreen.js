import React, { useState } from 'react';
import { View, Text, TextInput, TouchableOpacity, StyleSheet, Platform } from 'react-native';

export default function EditarFaltaScreen({ route, navigation }) {
  const { id } = route.params;

  const [qtd, setQtd] = useState("");
  const [dia, setDia] = useState("2025-11-20"); // formato YYYY-MM-DD

  function salvar() {
    navigation.goBack();
  }

  return (
    <View style={styles.container}>
      <View style={styles.box}>

        <Text style={styles.title}>Editar Falta</Text>
        <Text style={styles.sub}>ID do aluno: {id}</Text>

        <Text style={styles.label}>Qtd de faltas</Text>
        <TextInput
          style={styles.input}
          keyboardType="numeric"
          value={qtd}
          onChangeText={setQtd}
        />

        <Text style={styles.label}>Dia</Text>

        {Platform.OS === "web" ? (
          <input type="date" value={dia} onChange={(e) => setDia(e.target.value)}
            style={styles.date}
          />
        ) : (
          /* MOBILE → exibe formato BR */
          <TouchableOpacity style={styles.inputFake}>
            <Text style={styles.inputText}>
              {new Date(dia).toLocaleDateString("pt-BR")}
            </Text>
          </TouchableOpacity>
        )}

        <TouchableOpacity style={styles.btn} onPress={salvar}>
          <Text style={styles.btnText}>Salvar alterações</Text>
        </TouchableOpacity>

      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, justifyContent: 'center', backgroundColor: "#faf0ff" },

  box: {
    backgroundColor: '#fff',
    margin: 20,
    padding: 25,
    borderRadius: 12,
    elevation: 4
  },

  title: { textAlign: 'center', fontSize: 24 },
  sub: { textAlign: 'center', marginBottom: 20 },

  label: { fontWeight: 'bold', marginTop: 10 },

  input: {
    borderWidth: 1,
    padding: 10,
    borderRadius: 8,
    marginTop: 5,
    borderColor: '#aaa'
  },
  date:{
    width: "100%",
    padding: 12,
    borderRadius: 8,
    borderColor: "#aaa",
    borderWidth: 1,
    marginTop: 5,
    fontSize: 16
  },
  inputFake: {
    borderWidth: 1,
    padding: 12,
    borderRadius: 8,
    marginTop: 5,
    backgroundColor: "#f1f1f1",
    borderColor: "#aaa"
  },

  inputText: { fontSize: 16 },

  btn: {
    marginTop: 20,
    backgroundColor: "purple",
    padding: 15,
    borderRadius: 8
  },

  btnText: {
    color: "#fff",
    textAlign: "center",
    fontWeight: "bold"
  }
});
