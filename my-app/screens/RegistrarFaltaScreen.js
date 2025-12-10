import React, { useState } from 'react';
import { View, Text, TextInput, TouchableOpacity, StyleSheet, Platform } from 'react-native';

export default function RegistrarFaltaScreen({ route, navigation }) {
  const { id } = route.params;

  const [qtd, setQtd] = useState('');
  const [data, setData] = useState(new Date());

  function registrar() {
    navigation.goBack();
  }

  return (
    <View style={styles.container}>
      <View style={styles.box}>

        <Text style={styles.title}>Registrar Falta</Text>
        <Text style={styles.sub}>ID do aluno: {id}</Text>

        <Text style={styles.label}>Qtd de faltas</Text>
        <TextInput style={styles.input} keyboardType="numeric" value={qtd} onChangeText={setQtd} />

        <Text style={styles.label}>Data</Text>

        {Platform.OS === "web" ? (
          <input type="date" value={data.toISOString().split("T")[0]} onChange={(e) => setData(new Date(e.target.value))}
            style={styles.date}/>

        ) : (
          <TouchableOpacity style={styles.inputFake}>
            <Text style={styles.inputText}>
              {data.toLocaleDateString("pt-BR")}
            </Text>
          </TouchableOpacity>
        )}

        <TouchableOpacity style={styles.btn} onPress={registrar}>
          <Text style={styles.btnText}>Registrar</Text>
        </TouchableOpacity>

      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, justifyContent: 'center', backgroundColor: "#F3E5F5" },

  box: { 
    backgroundColor: '#fff', 
    margin: 20, 
    padding: 25, 
    borderRadius: 20, 
    elevation: 6 
  },

  title: { 
    textAlign: 'center', 
    fontSize: 26, 
    marginBottom: 8,
    fontWeight: "bold",
    color: "#512DA8"
  },

  sub: { 
    textAlign: 'center', 
    marginBottom: 20,
    color: "#5E35B1"
  },

  label: { 
    fontWeight: '700', 
    marginTop: 10,
    color: "#5E35B1"
  },

  input: {
    borderWidth: 2,
    padding: 12,
    borderRadius: 10,
    marginTop: 5,
    borderColor: '#9575CD'
  },

  date: {
    width: "100%",
    padding: 12,
    borderRadius: 10,
    borderColor: "#9575CD",
    borderWidth: 2,
    marginTop: 5,
    fontSize: 16
  },

  inputFake: {
    borderWidth: 2,
    padding: 12,
    borderRadius: 10,
    marginTop: 5,
    backgroundColor: "#f8f1ff",
    borderColor: "#9575CD"
  },

  inputText: { fontSize: 16 },

  btn: { 
    marginTop: 20, 
    backgroundColor: "#673AB7", 
    padding: 15, 
    borderRadius: 12 
  },

  btnText: { 
    color: "#fff", 
    textAlign: "center", 
    fontWeight: "bold",
    fontSize: 16
  }
});
