import networkx as nx
import numpy as np

class Mytextrank(object):
    s_k_pos =  ['IC', 'JKS', 'JKC', 'JKG', 'JKO', 'JKB', 'JKV', 'JKQ', 'JC', 'JX', 'XR', 'SF', 'SE', 'SSO', 'SSC', 'SC',
           'SY', 'EC', 'EF', 'ETN', 'ETM', 'XSV', 'XSA', 'XSN', 'XPN', 'NP']

    def __init__(self, stopword, stop_pos=s_k_pos, mecab_path="/usr/local/lib/mecab/dic/mecab-ko-dic"):
        self.stopward = stopword
        self.stop_pos = stop_pos
        from konlpy.tag import Mecab
        self.pos_tag = Mecab(mecab_path)
        self.max = 5
        #self.lang ='ko'
        self.graph = {}
        self._node = {}
        self._adj = {}

    def _word_tokenize(self, *args):
        import nltk.tokenize
        #print(len(args))
        sents = nltk.tokenize.word_tokenize(*args)
        return sents

    def _sent_tokenize(self, *args):
        import nltk.tokenize
        sents = nltk.tokenize.sent_tokenize(*args)
        return sents

    def build_keywords(self, text, processed=False):
        #tokenize by word
        #pos tagging
        #stopwords filltering
        #stop pos filltering
        import time
        total = time.time()
        nodes = []
        tokens = []

        if not processed:
            dsents = self._word_tokenize(text)
            for sent in dsents:
                token = self.pos_tag.pos(sent)[0]
                if (len(token[0]) > 1) & (str(token[0]) not in self.stopward) & (
                        token[1][:3] not in self.stop_pos) & (
                        token[0] != token[1]):
                    nodes.append(token)
                tokens.append(token)
        else:
            token = text
            if (len(token[0]) > 1) & (str(token[0]) not in self.stopward) & (
                    token[1][:3] not in self.stop_pos) & (
                    token[0] != token[1]):
                nodes.append(token)
            tokens.append(token)

        end = time.time()
        print(f'total time :{end-total:.4f}')
        return nodes, tokens

    def make_graph(self, nodes, tokens):
        for n in nodes:

            if n not in self._node:
                self._adj[n] = []
                self._node[n] = self._adj[n]
            else:
                self._node[n].append(n)
        #print(f'count {len(self._node)} _node {self._node}')
        #print(f'count {len(self._adj)} _adj {self._adj}')

    def _stopword_fillter(self, *args):
        nodes = []
        tokens = []
        for token in args:

            if (len(token[0]) > 1) & (str(token[0]) not in self.stopward) & (
                    token[1][:3] not in self.stop_pos) & (
                    token[0] != token[1]):
                nodes.append(token)

            tokens.append(token)
            self.tokens.append(token[0])
            return nodes, tokens

    def _connect(self, nodes, tokens):
        edges = []
        for window_start in range(0, (len(tokens) - 10 + 1)):
            pass

class SimpleTextRank(object):
    pos = ['IC', 'JKS', 'JKC', 'JKG', 'JKO', 'JKB', 'JKV', 'JKQ', 'JC', 'JX', 'XR',
               'SF', 'SE', 'SSO', 'SSC', 'SC',
               'SY', 'EC', 'EF', 'ETN', 'ETM', 'XSV', 'XSA', 'XSN', 'XPN', 'NP']

    def __init__(self,STOPWORD=None, STOPPOS=pos, MECABPATH=None):
        from konlpy.tag import Mecab

        self.stopwords = STOPWORD
        self.stoppos = STOPPOS
        self.mecabpath = MECABPATH
        self.pos_tag = Mecab(self.mecabpath)
        self.graph = {}
        self.graph_treform =nx.diamond_graph()
        self.graph_treform.clear()


    def process(self, text):
        dsents = self._word_tokenize(text)
        nodes, tokens = self.build_keywords(dsents)
        self._make_graph(nodes, tokens)

        tr = self.myscores()

        result = sorted(tr, key=lambda x: x[1], reverse=True)

        return result[:5]

    def network_process(self,text):
        dsents = self._word_tokenize(text)
        nodes, tokens = self.build_keywords(dsents)
        self._network_make_graph(nodes, tokens)
        result = self.network_score()
        return result[:5]

    def _network_make_graph(self, n, t):
        self.graph_treform.add_nodes_from(list(set(n)))  # node 등록
        self.graph_treform.add_edges_from(self._connect(n, t))

    def network_score(self):
        scores = nx.pagerank(self.graph_treform)
        rank = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        return [(word[0],tr) for word, tr in rank]

    def _word_tokenize(self, *args):
        import nltk.tokenize
        sents = nltk.tokenize.word_tokenize(*args)
        return sents

    def _sent_tokenize(self, *args):
        import nltk.tokenize
        sents = nltk.tokenize.sent_tokenize(*args)
        return sents

    def build_keywords(self, text):
        nodes = []
        tokens = []
        dsents = text

        for sent in dsents:
            token = self.pos_tag.pos(sent)[0]
            if (len(token[0]) > 1) & (str(token[0]) not in self.stopwords) & (
                    token[1][:3] not in self.stoppos) & (
                    token[0] != token[1]):
                nodes.append(token)
            tokens.append(token)
        return nodes, tokens

    def _make_node(self, n):
        inner_nodes = set(n)
        for node in inner_nodes:
            out = dict((i, 0) for i in inner_nodes)
            self.graph[node] = out

    def _connect(self, nodes, tokens):
        edges = []
        window_size = 10
        for window_start in range(0, (len(tokens) - window_size + 1)):
            window = tokens[window_start:window_start + window_size]

            for i in range(window_size):
                for j in range(window_size):
                    if (i > j) & (window[i] in nodes) & (window[j] in nodes):
                        edges.append((window[i], window[j]))
        return edges

    def _make_graph(self, n, t):


        self._make_node(n)
        connected = self._connect(n, t)

        for attr in connected:
            self.graph[attr[0]].update({attr[1]: 1})



    def myscores(self):
        d = 0.85  # damping facotr
        textrank = []
        pr = np.array([1 for _ in range(len(self.graph))])
        label = []
        g = []

        for inV, outV in self.graph.items():
            label.append(inV[0])
            g.append(np.array([i for i in outV.values()]))

        g = self._nomalize_column(g)
        for iter in range(10):
            #pr = np.transpose(pr)
            pr = (1-d) * d * np.dot(g, pr)

        textrank = zip(label, pr)


        return textrank


    def _nomalize_column(self, g):
        x = np.array(g)

        x_normed = x / x.sum(axis=1)
        return x_normed
        # for idx, row in enumerate(mat):
        #     N = sum([1 for i in row if i > 0])
        #
        #     mat[idx] = mat[idx] * (1/N)

        # for inV, outV in self.graph.items():
        #     N = sum([1 for i in outV.values() if i > 0])
        #     for attr, val in outV.items():
        #         self.graph[inV][attr] = round(val / (N+1), 10)

