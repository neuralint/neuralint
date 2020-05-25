<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<gxl xmlns="http://www.gupro.de/GXL/gxl-1.0.dtd">
    <graph role="graph" edgeids="false" edgemode="directed" id="s13">
        <attr name="$version">
            <string>curly</string>
        </attr>
        <node id="n0">
            <attr name="layout">
                <string>14 13 88 18</string>
            </attr>
        </node>
        <node id="n26">
            <attr name="layout">
                <string>103 159 129 36</string>
            </attr>
        </node>
        <node id="n27">
            <attr name="layout">
                <string>20 97 46 18</string>
            </attr>
        </node>
        <node id="n28">
            <attr name="layout">
                <string>280 32 66 72</string>
            </attr>
        </node>
        <node id="n29">
            <attr name="layout">
                <string>456 26 93 144</string>
            </attr>
        </node>
        <node id="n30">
            <attr name="layout">
                <string>630 162 56 36</string>
            </attr>
        </node>
        <node id="n31">
            <attr name="layout">
                <string>629 78 42 36</string>
            </attr>
        </node>
        <node id="n32">
            <attr name="layout">
                <string>641 31 25 18</string>
            </attr>
        </node>
        <node id="n33">
            <attr name="layout">
                <string>465 283 93 126</string>
            </attr>
        </node>
        <node id="n34">
            <attr name="layout">
                <string>299 348 31 36</string>
            </attr>
        </node>
        <node id="n35">
            <attr name="layout">
                <string>634 474 56 36</string>
            </attr>
        </node>
        <node id="n36">
            <attr name="layout">
                <string>284 445 64 36</string>
            </attr>
        </node>
        <node id="n37">
            <attr name="layout">
                <string>628 345 58 36</string>
            </attr>
        </node>
        <node id="n38">
            <attr name="layout">
                <string>432 480 108 36</string>
            </attr>
        </node>
        <edge from="n0" to="n0">
            <attr name="label">
                <string>type:DNN-program</string>
            </attr>
        </edge>
        <edge from="n0" to="n26">
            <attr name="label">
                <string>has</string>
            </attr>
        </edge>
        <edge from="n0" to="n27">
            <attr name="label">
                <string>has</string>
            </attr>
        </edge>
        <edge from="n26" to="n26">
            <attr name="label">
                <string>type:Model</string>
            </attr>
        </edge>
        <edge from="n26" to="n26">
            <attr name="label">
                <string>let:hiddenLayerCount = int:1</string>
            </attr>
        </edge>
        <edge from="n26" to="n28">
            <attr name="label">
                <string>starts</string>
            </attr>
        </edge>
        <edge from="n27" to="n27">
            <attr name="label">
                <string>type:Learner</string>
            </attr>
        </edge>
        <edge from="n28" to="n28">
            <attr name="label">
                <string>type:InputLayer</string>
            </attr>
        </edge>
        <edge from="n28" to="n28">
            <attr name="label">
                <string>flag:done</string>
            </attr>
        </edge>
        <edge from="n28" to="n28">
            <attr name="label">
                <string>let:No = int:1</string>
            </attr>
        </edge>
        <edge from="n28" to="n28">
            <attr name="label">
                <string>let:size = string:"n1"</string>
            </attr>
        </edge>
        <edge from="n28" to="n29">
            <attr name="label">
                <string>has-some</string>
            </attr>
        </edge>
        <edge from="n29" to="n29">
            <attr name="label">
                <string>type:Layer</string>
            </attr>
        </edge>
        <edge from="n29" to="n29">
            <attr name="label">
                <string>flag:done</string>
            </attr>
        </edge>
        <edge from="n29" to="n29">
            <attr name="label">
                <string>flag:noConstraint</string>
            </attr>
        </edge>
        <edge from="n29" to="n29">
            <attr name="label">
                <string>flag:noInitial</string>
            </attr>
        </edge>
        <edge from="n29" to="n29">
            <attr name="label">
                <string>flag:noRegularizer</string>
            </attr>
        </edge>
        <edge from="n29" to="n29">
            <attr name="label">
                <string>let:No = int:2</string>
            </attr>
        </edge>
        <edge from="n29" to="n29">
            <attr name="label">
                <string>let:inputSize = string:"n1"</string>
            </attr>
        </edge>
        <edge from="n29" to="n29">
            <attr name="label">
                <string>let:size = string:"n2"</string>
            </attr>
        </edge>
        <edge from="n29" to="n30">
            <attr name="label">
                <string>has-a</string>
            </attr>
        </edge>
        <edge from="n29" to="n33">
            <attr name="label">
                <string>next</string>
            </attr>
        </edge>
        <edge from="n29" to="n32">
            <attr name="label">
                <string>has-a</string>
            </attr>
        </edge>
        <edge from="n29" to="n31">
            <attr name="label">
                <string>has-a</string>
            </attr>
        </edge>
        <edge from="n30" to="n30">
            <attr name="label">
                <string>type:Activator</string>
            </attr>
        </edge>
        <edge from="n30" to="n30">
            <attr name="label">
                <string>flag:relu</string>
            </attr>
        </edge>
        <edge from="n32" to="n32">
            <attr name="label">
                <string>type:Bias</string>
            </attr>
        </edge>
        <edge from="n33" to="n33">
            <attr name="label">
                <string>type:Layer</string>
            </attr>
        </edge>
        <edge from="n33" to="n33">
            <attr name="label">
                <string>flag:end</string>
            </attr>
        </edge>
        <edge from="n33" to="n33">
            <attr name="label">
                <string>flag:noBias</string>
            </attr>
        </edge>
        <edge from="n33" to="n33">
            <attr name="label">
                <string>flag:output</string>
            </attr>
        </edge>
        <edge from="n33" to="n33">
            <attr name="label">
                <string>let:No = int:3</string>
            </attr>
        </edge>
        <edge from="n33" to="n33">
            <attr name="label">
                <string>let:inputSize = string:"n2"</string>
            </attr>
        </edge>
        <edge from="n33" to="n33">
            <attr name="label">
                <string>let:size = string:"n3"</string>
            </attr>
        </edge>
        <edge from="n33" to="n37">
            <attr name="label">
                <string>has-a</string>
            </attr>
        </edge>
        <edge from="n33" to="n38">
            <attr name="label">
                <string>has-a</string>
            </attr>
        </edge>
        <edge from="n33" to="n36">
            <attr name="label">
                <string>has-a</string>
            </attr>
        </edge>
        <edge from="n33" to="n34">
            <attr name="label">
                <string>has-a</string>
            </attr>
        </edge>
        <edge from="n33" to="n35">
            <attr name="label">
                <string>has-a</string>
            </attr>
        </edge>
        <edge from="n34" to="n34">
            <attr name="label">
                <string>type:Type</string>
            </attr>
        </edge>
        <edge from="n34" to="n34">
            <attr name="label">
                <string>flag:dense</string>
            </attr>
        </edge>
        <edge from="n35" to="n35">
            <attr name="label">
                <string>type:Activator</string>
            </attr>
        </edge>
        <edge from="n35" to="n35">
            <attr name="label">
                <string>flag:softmax</string>
            </attr>
        </edge>
        <edge from="n36" to="n36">
            <attr name="label">
                <string>type:Constraint</string>
            </attr>
        </edge>
        <edge from="n36" to="n36">
            <attr name="label">
                <string>flag:MaxNorm</string>
            </attr>
        </edge>
        <edge from="n37" to="n37">
            <attr name="label">
                <string>type:Initializer</string>
            </attr>
        </edge>
        <edge from="n37" to="n37">
            <attr name="label">
                <string>flag:constant</string>
            </attr>
        </edge>
        <edge from="n38" to="n38">
            <attr name="label">
                <string>type:Regularizer</string>
            </attr>
        </edge>
        <edge from="n38" to="n38">
            <attr name="label">
                <string>let:dropoutRate = real:0.4</string>
            </attr>
        </edge>
    </graph>
</gxl>
