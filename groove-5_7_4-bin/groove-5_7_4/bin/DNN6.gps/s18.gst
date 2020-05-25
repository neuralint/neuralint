<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<gxl xmlns="http://www.gupro.de/GXL/gxl-1.0.dtd">
    <graph role="graph" edgeids="false" edgemode="directed" id="s18">
        <attr name="$version">
            <string>curly</string>
        </attr>
        <node id="n0">
            <attr name="layout">
                <string>32 21 88 18</string>
            </attr>
        </node>
        <node id="n11">
            <attr name="layout">
                <string>88 97 129 36</string>
            </attr>
        </node>
        <node id="n12">
            <attr name="layout">
                <string>25 100 46 18</string>
            </attr>
        </node>
        <node id="n13">
            <attr name="layout">
                <string>263 16 66 72</string>
            </attr>
        </node>
        <node id="n15">
            <attr name="layout">
                <string>431 12 93 162</string>
            </attr>
        </node>
        <node id="n16">
            <attr name="layout">
                <string>620 68 35 36</string>
            </attr>
        </node>
        <node id="n17">
            <attr name="layout">
                <string>578 13 56 36</string>
            </attr>
        </node>
        <node id="n20">
            <attr name="layout">
                <string>613 210 93 144</string>
            </attr>
        </node>
        <node id="n21">
            <attr name="layout">
                <string>641 538 31 36</string>
            </attr>
        </node>
        <node id="n22">
            <attr name="layout">
                <string>553 529 56 36</string>
            </attr>
        </node>
        <node id="n26">
            <attr name="layout">
                <string>684 417 58 36</string>
            </attr>
        </node>
        <node id="n27">
            <attr name="layout">
                <string>440 253 93 144</string>
            </attr>
        </node>
        <node id="n28">
            <attr name="layout">
                <string>261 296 42 36</string>
            </attr>
        </node>
        <node id="n29">
            <attr name="layout">
                <string>326 193 56 36</string>
            </attr>
        </node>
        <node id="n33">
            <attr name="layout">
                <string>281 251 25 18</string>
            </attr>
        </node>
        <node id="n34">
            <attr name="layout">
                <string>281 429 93 162</string>
            </attr>
        </node>
        <node id="n35">
            <attr name="layout">
                <string>107 524 31 36</string>
            </attr>
        </node>
        <node id="n36">
            <attr name="layout">
                <string>148 476 56 36</string>
            </attr>
        </node>
        <node id="n37">
            <attr name="layout">
                <string>28 428 108 36</string>
            </attr>
        </node>
        <edge from="n0" to="n12">
            <attr name="label">
                <string>has</string>
            </attr>
        </edge>
        <edge from="n0" to="n11">
            <attr name="label">
                <string>has</string>
            </attr>
        </edge>
        <edge from="n0" to="n0">
            <attr name="label">
                <string>type:DNN-program</string>
            </attr>
        </edge>
        <edge from="n11" to="n13">
            <attr name="label">
                <string>starts</string>
            </attr>
        </edge>
        <edge from="n11" to="n11">
            <attr name="label">
                <string>type:Model</string>
            </attr>
        </edge>
        <edge from="n11" to="n11">
            <attr name="label">
                <string>let:hiddenLayerCount = int:3</string>
            </attr>
        </edge>
        <edge from="n12" to="n12">
            <attr name="label">
                <string>type:Learner</string>
            </attr>
        </edge>
        <edge from="n13" to="n13">
            <attr name="label">
                <string>flag:done</string>
            </attr>
        </edge>
        <edge from="n13" to="n13">
            <attr name="label">
                <string>let:size = string:"n1"</string>
            </attr>
        </edge>
        <edge from="n13" to="n13">
            <attr name="label">
                <string>let:No = int:1</string>
            </attr>
        </edge>
        <edge from="n13" to="n13">
            <attr name="label">
                <string>type:InputLayer</string>
            </attr>
        </edge>
        <edge from="n13" to="n15">
            <attr name="label">
                <string>has-some</string>
            </attr>
        </edge>
        <edge from="n15" to="n20">
            <attr name="label">
                <string>next</string>
            </attr>
        </edge>
        <edge from="n15" to="n15">
            <attr name="label">
                <string>let:size = string:"n2"</string>
            </attr>
        </edge>
        <edge from="n15" to="n15">
            <attr name="label">
                <string>let:inputSize = string:"n1"</string>
            </attr>
        </edge>
        <edge from="n15" to="n15">
            <attr name="label">
                <string>let:No = int:2</string>
            </attr>
        </edge>
        <edge from="n15" to="n15">
            <attr name="label">
                <string>flag:done</string>
            </attr>
        </edge>
        <edge from="n15" to="n15">
            <attr name="label">
                <string>flag:noBias</string>
            </attr>
        </edge>
        <edge from="n15" to="n15">
            <attr name="label">
                <string>flag:noInitial</string>
            </attr>
        </edge>
        <edge from="n15" to="n17">
            <attr name="label">
                <string>has-a</string>
            </attr>
        </edge>
        <edge from="n15" to="n16">
            <attr name="label">
                <string>has-a</string>
            </attr>
        </edge>
        <edge from="n15" to="n15">
            <attr name="label">
                <string>type:Layer</string>
            </attr>
        </edge>
        <edge from="n15" to="n15">
            <attr name="label">
                <string>flag:noConstraint</string>
            </attr>
        </edge>
        <edge from="n15" to="n15">
            <attr name="label">
                <string>flag:noRegularizer</string>
            </attr>
        </edge>
        <edge from="n16" to="n16">
            <attr name="label">
                <string>flag:flatten</string>
            </attr>
        </edge>
        <edge from="n16" to="n16">
            <attr name="label">
                <string>type:Type</string>
            </attr>
        </edge>
        <edge from="n17" to="n17">
            <attr name="label">
                <string>type:Activator</string>
            </attr>
        </edge>
        <edge from="n17" to="n17">
            <attr name="label">
                <string>flag:relu</string>
            </attr>
        </edge>
        <edge from="n20" to="n20">
            <attr name="label">
                <string>let:inputSize = string:"n2"</string>
            </attr>
        </edge>
        <edge from="n20" to="n27">
            <attr name="label">
                <string>next</string>
            </attr>
        </edge>
        <edge from="n20" to="n21">
            <attr name="label">
                <string>has-a</string>
            </attr>
        </edge>
        <edge from="n20" to="n20">
            <attr name="label">
                <string>flag:noConstraint</string>
            </attr>
        </edge>
        <edge from="n20" to="n20">
            <attr name="label">
                <string>type:Layer</string>
            </attr>
        </edge>
        <edge from="n20" to="n20">
            <attr name="label">
                <string>flag:noRegularizer</string>
            </attr>
        </edge>
        <edge from="n20" to="n22">
            <attr name="label">
                <string>has-a</string>
            </attr>
        </edge>
        <edge from="n20" to="n26">
            <attr name="label">
                <string>has-a</string>
            </attr>
        </edge>
        <edge from="n20" to="n20">
            <attr name="label">
                <string>let:No = int:3</string>
            </attr>
        </edge>
        <edge from="n20" to="n20">
            <attr name="label">
                <string>flag:done</string>
            </attr>
        </edge>
        <edge from="n20" to="n20">
            <attr name="label">
                <string>let:size = string:"n3"</string>
            </attr>
        </edge>
        <edge from="n20" to="n20">
            <attr name="label">
                <string>flag:noBias</string>
            </attr>
        </edge>
        <edge from="n21" to="n21">
            <attr name="label">
                <string>type:Type</string>
            </attr>
        </edge>
        <edge from="n21" to="n21">
            <attr name="label">
                <string>flag:dense</string>
            </attr>
        </edge>
        <edge from="n22" to="n22">
            <attr name="label">
                <string>type:Activator</string>
            </attr>
        </edge>
        <edge from="n22" to="n22">
            <attr name="label">
                <string>flag:relu</string>
            </attr>
        </edge>
        <edge from="n26" to="n26">
            <attr name="label">
                <string>flag:zeros</string>
            </attr>
        </edge>
        <edge from="n26" to="n26">
            <attr name="label">
                <string>type:Initializer</string>
            </attr>
        </edge>
        <edge from="n27" to="n34">
            <attr name="label">
                <string>next</string>
            </attr>
        </edge>
        <edge from="n27" to="n27">
            <attr name="label">
                <string>flag:noConstraint</string>
            </attr>
        </edge>
        <edge from="n27" to="n29">
            <attr name="label">
                <string>has-a</string>
            </attr>
        </edge>
        <edge from="n27" to="n27">
            <attr name="label">
                <string>flag:noRegularizer</string>
            </attr>
        </edge>
        <edge from="n27" to="n27">
            <attr name="label">
                <string>let:size = string:"n4"</string>
            </attr>
        </edge>
        <edge from="n27" to="n27">
            <attr name="label">
                <string>let:inputSize = string:"n3"</string>
            </attr>
        </edge>
        <edge from="n27" to="n27">
            <attr name="label">
                <string>let:No = int:4</string>
            </attr>
        </edge>
        <edge from="n27" to="n33">
            <attr name="label">
                <string>has-a</string>
            </attr>
        </edge>
        <edge from="n27" to="n28">
            <attr name="label">
                <string>has-a</string>
            </attr>
        </edge>
        <edge from="n27" to="n27">
            <attr name="label">
                <string>type:Layer</string>
            </attr>
        </edge>
        <edge from="n27" to="n27">
            <attr name="label">
                <string>flag:noInitial</string>
            </attr>
        </edge>
        <edge from="n27" to="n27">
            <attr name="label">
                <string>flag:done</string>
            </attr>
        </edge>
        <edge from="n28" to="n28">
            <attr name="label">
                <string>flag:conv1D</string>
            </attr>
        </edge>
        <edge from="n28" to="n28">
            <attr name="label">
                <string>type:Type</string>
            </attr>
        </edge>
        <edge from="n29" to="n29">
            <attr name="label">
                <string>type:Activator</string>
            </attr>
        </edge>
        <edge from="n29" to="n29">
            <attr name="label">
                <string>flag:relu</string>
            </attr>
        </edge>
        <edge from="n33" to="n33">
            <attr name="label">
                <string>type:Bias</string>
            </attr>
        </edge>
        <edge from="n34" to="n34">
            <attr name="label">
                <string>flag:output</string>
            </attr>
        </edge>
        <edge from="n34" to="n34">
            <attr name="label">
                <string>let:inputSize = string:"n4"</string>
            </attr>
        </edge>
        <edge from="n34" to="n36">
            <attr name="label">
                <string>has-a</string>
            </attr>
        </edge>
        <edge from="n34" to="n34">
            <attr name="label">
                <string>flag:noInitial</string>
            </attr>
        </edge>
        <edge from="n34" to="n37">
            <attr name="label">
                <string>has-a</string>
            </attr>
        </edge>
        <edge from="n34" to="n34">
            <attr name="label">
                <string>type:Layer</string>
            </attr>
        </edge>
        <edge from="n34" to="n34">
            <attr name="label">
                <string>let:size = string:"n5"</string>
            </attr>
        </edge>
        <edge from="n34" to="n34">
            <attr name="label">
                <string>let:No = int:5</string>
            </attr>
        </edge>
        <edge from="n34" to="n34">
            <attr name="label">
                <string>flag:noConstraint</string>
            </attr>
        </edge>
        <edge from="n34" to="n34">
            <attr name="label">
                <string>flag:end</string>
            </attr>
        </edge>
        <edge from="n34" to="n35">
            <attr name="label">
                <string>has-a</string>
            </attr>
        </edge>
        <edge from="n34" to="n34">
            <attr name="label">
                <string>flag:noBias</string>
            </attr>
        </edge>
        <edge from="n35" to="n35">
            <attr name="label">
                <string>type:Type</string>
            </attr>
        </edge>
        <edge from="n35" to="n35">
            <attr name="label">
                <string>flag:dense</string>
            </attr>
        </edge>
        <edge from="n36" to="n36">
            <attr name="label">
                <string>type:Activator</string>
            </attr>
        </edge>
        <edge from="n36" to="n36">
            <attr name="label">
                <string>flag:softmax</string>
            </attr>
        </edge>
        <edge from="n37" to="n37">
            <attr name="label">
                <string>type:Regularizer</string>
            </attr>
        </edge>
        <edge from="n37" to="n37">
            <attr name="label">
                <string>let:dropoutRate = real:0.4</string>
            </attr>
        </edge>
    </graph>
</gxl>
