import os, sys
import tensorflow as tensorflow
import urllib

RETRAINED_LABELS = os.path.join(os.path.dirname(__file__), 'retrained_labels.txt')
RETRAINED_GRAPH = os.path.join(os.path.dirname(__file__), 'retrained_graph.pb')

class ClassifyImg(object):

    
    def __init__(self):
        self.label_lines = [line.rstrip() for line
                            in tensorflow.gfile.GFile(RETRAINED_LABELS)]
        
        with tensorflow.gfile.FastGFile(RETRAINED_GRAPH, 'rb') as f:
            graph_def = tensorflow.GraphDef()
            graph_def.ParseFromString(f.read())
            tensorflow.import_graph_def(graph_def, name='')

    def classify_image(self, image_path):

        f_score = {}
        try:
            image_data = urllib.urlopen(image_path).read()
        except ValueError:
            image_data = tensorflow.gfile.FastGFile(image_path, 'rb').read()
            
        with tensorflow.Session() as sess:
            softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
                
            predictions = sess.run(softmax_tensor, {'DecodeJpeg/contents:0': image_data})
            top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]
            
            for node_id in top_k:
                human_string = self.label_lines[node_id]
                score = predictions[0][node_id]
                print('%s (score = %.5f)' % (human_string, score))
                f_score[human_string] = score

        return f_score
