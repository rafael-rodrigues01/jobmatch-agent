# Quickstart & Validation Guide: Correção do Erro de Carregamento do Perfil

**Feature**: `002-fix-profile-load-error`  
**Date**: 2026-11-06  

Este guia valida os cenários de resiliência e tratamento de erro de conexão entre frontend e backend.

## 1. Cenário de Validação A: Backend Offline (Feedback e Retry)

### Objetivo
Validar que, quando o frontend é iniciado sem o backend em execução, a aplicação não trava e exibe o banner informativo com botão de recarga.

### Passos
1. Certifique-se de que nenhum serviço uvicorn está rodando na porta 8000.
2. Inicie o frontend:
   ```powershell
   cd frontend
   npm run dev
   ```
3. Abra `http://localhost:5173` no navegador.
4. **Resultado Esperado**:
   - O frontend renderiza a tela normalmente.
   - Um banner contextualizado com borda amarela/vermelha (Design System) é exibido informando: *"Serviço local indisponível. Verifique se o backend está em execução na porta 8000."*
   - O botão **"Tentar novamente"** está visível e acessível.
   - Os campos do formulário continuam utilizáveis.

5. Em outro terminal, inicie o backend:
   ```powershell
   cd backend
   .\.venv\Scripts\Activate.ps1
   uvicorn app.main:app --port 8000 --reload
   ```
6. Clique no botão **"Tentar novamente"** no frontend.
7. **Resultado Esperado**:
   - O banner de erro desaparece instantaneamente sem necessidade de recarregar o navegador.
   - Os dados do perfil são carregados (ou o formulário fica pronto para preenchimento).

---

## 2. Cenário de Validação B: Fallback Local do Banco de Dados (SQLite)

### Objetivo
Validar que o backend inicializa e funciona mesmo se o serviço do PostgreSQL estiver parado na máquina do usuário.

### Passos
1. No terminal do backend, execute sem PostgreSQL:
   ```powershell
   cd backend
   .\.venv\Scripts\Activate.ps1
   python -m uvicorn app.main:app --port 8000
   ```
2. Verifique o endpoint de saúde:
   ```powershell
   curl http://localhost:8000/health
   ```
3. Faça uma chamada no perfil:
   ```powershell
   curl http://localhost:8000/api/v1/profile
   ```
4. **Resultado Esperado**:
   - A API responde com HTTP 200 (ou 404 caso seja perfil novo), sem crash e sem `OperationalError: Connection refused`.

---

## 3. Testes Automatizados da Tríade de Qualidade

Execute a suíte para garantir que nada quebrou:

```powershell
# 1. Backend (Pytest)
cd backend
.\.venv\Scripts\pytest

# 2. Frontend (Vitest & Build)
cd ../frontend
npm test -- --run
npm run build
```

