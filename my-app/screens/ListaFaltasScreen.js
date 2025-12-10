import React from 'react';
import { View, Text, StyleSheet, ScrollView, TouchableOpacity } from 'react-native';

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

// MOCK das faltas
const faltasMock = {
  1: [
    { id: 1, dia: "2025-11-10", qtd: 1 },
    { id: 2, dia: "2025-11-20", qtd: 2 },
    { id: 3, dia: "2025-12-02", qtd: 1 },
  ],
  2: [
    { id: 1, dia: "2025-10-01", qtd: 1 },
    { id: 2, dia: "2025-10-15", qtd: 1 },
  ],
  3: [
    { id: 1, dia: "2025-09-10", qtd: 3 }
  ]
};

export default function ListaFaltasScreen({ route, navigation }) {
  const { id } = route.params;

  const aluno = alunos.find(a => a.id === id);
  const faltas = faltasMock[id] || [];

  // soma total das faltas
  const totalFaltas = faltas.reduce((sum, f) => sum + f.qtd, 0);

  return (
    <View style={styles.container}>
      
      <Text style={styles.title}>Faltas do Aluno</Text>

      {/* Nome e total */}
      <Text style={styles.alunoNome}>{aluno ? aluno.nome : "Aluno não encontrado"}</Text>
      <Text style={styles.totalFaltas}>Total de faltas: {totalFaltas}</Text>

      <ScrollView style={styles.scroll}>
        {faltas.length === 0 ? (
          <Text style={styles.noData}>Nenhuma falta registrada.</Text>
        ) : (
          faltas.map(f => (
            <View key={f.id} style={styles.card}>

              <Text style={styles.cardTitle}>
                Dia: {new Date(f.dia).toLocaleDateString("pt-BR")}
              </Text>

              <Text style={styles.info}>Quantidade: {f.qtd}</Text>

              <TouchableOpacity
                onPress={() => navigation.navigate("EditarFalta", {
                  id: id,
                  faltaId: f.id,
                  qtd: f.qtd,
                  dia: f.dia
                })}
              >
                <Text style={styles.edit}>Editar falta</Text>
              </TouchableOpacity>

            </View>
          ))
        )}
      </ScrollView>

    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, padding: 20, backgroundColor: "#F3E5F5" },

  title: { 
    fontSize: 26, 
    textAlign: "center", 
    marginBottom: 5,
    color: "#512DA8",
    fontWeight: "bold"
  },

  alunoNome: {
    textAlign: "center",
    fontSize: 20,
    fontWeight: "bold",
    marginBottom: 5,
    color: "#311B92"
  },

  totalFaltas: {
    textAlign: "center",
    fontSize: 16,
    marginBottom: 20,
    color: "#5E35B1"
  },

  card: {
    backgroundColor: "#fff",
    padding: 18,
    borderRadius: 16,
    marginBottom: 15,
    elevation: 5
  },

  cardTitle: { 
    fontSize: 17, 
    fontWeight: "bold",
    color: "#4527A0"
  },

  info: { 
    marginTop: 5, 
    marginBottom: 10, 
    color: "#555" 
  },

  edit: { 
    color: "#7E57C2", 
    fontWeight: "700" 
  },

  noData: {
    textAlign: "center",
    marginTop: 40,
    fontSize: 16,
    color: "#777"
  }
});
