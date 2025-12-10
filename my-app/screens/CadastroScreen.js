import React, { useState } from 'react';
import { View, Text, TextInput, TouchableOpacity, StyleSheet } from 'react-native';

export default function CadastroScreen({ navigation }) {
  const [form, setForm] = useState({
    login: "",
    senha: "",
    nome: "",
    email: ""
  });

  function alterar(campo, valor) {
    setForm({ ...form, [campo]: valor });
  }

  function cadastrar() {
    navigation.navigate("Login");
  }

  return (
    <View style={styles.container}>
      <View style={styles.box}>
        <Text style={styles.title}>Cadastrar Docente</Text>

        <Text style={styles.label}>Login</Text>
        <TextInput style={styles.input} onChangeText={(v) => alterar("login", v)} />

        <Text style={styles.label}>Senha</Text>
        <TextInput style={styles.input} secureTextEntry onChangeText={(v) => alterar("senha", v)} />

        <Text style={styles.label}>Nome Completo</Text>
        <TextInput style={styles.input} onChangeText={(v) => alterar("nome", v)} />

        <Text style={styles.label}>Email</Text>
        <TextInput style={styles.input} onChangeText={(v) => alterar("email", v)} />

        <TouchableOpacity style={styles.btn} onPress={cadastrar}>
          <Text style={styles.btnText}>Cadastrar</Text>
        </TouchableOpacity>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: { 
    flex: 1, 
    justifyContent: 'center', 
    backgroundColor: '#F3E5F5'
  },

  box: { 
    margin: 20, 
    padding: 28, 
    backgroundColor: '#fff', 
    borderRadius: 20, 
    elevation: 6 
  },

  title: { 
    fontSize: 26, 
    textAlign: 'center', 
    marginBottom: 25,
    color: '#512DA8',
    fontWeight: 'bold'
  },

  label: {
    fontWeight: '700',
    color: '#5E35B1'
  },

  input: { 
    borderWidth: 2, 
    padding: 12, 
    borderRadius: 10, 
    marginBottom: 15, 
    borderColor: '#9575CD' 
  },

  btn: { 
    backgroundColor: '#673AB7', 
    padding: 15, 
    borderRadius: 12 
  },

  btnText: { 
    color: '#fff', 
    textAlign: 'center', 
    fontWeight: 'bold',
    fontSize: 16
  }
});
